import os
import time
import pandas as pd
from docx import Document
from docx.shared import RGBColor
from openai import OpenAI
from tqdm import tqdm
import re

# Configuration
DATA_DIR = "data"
GENERATED_DIR = "generated_reports"
client = OpenAI(api_key="  here anouar")

os.makedirs(GENERATED_DIR, exist_ok=True)

def extract_findings_from_excel(file_path):
    df = pd.read_excel(file_path)
    findings = df.to_string(index=False)
    return findings

def format_section(paragraph, text):
    # Detect bold sub-sections like **Title:** and render them bold (but not blue)
    bold_matches = re.findall(r"\\*\\*(.*?)\\*\\*", text)
    for match in bold_matches:
        text = text.replace(f"**{match}**", match)

    parts = re.split(r"(\\*\\*.*?\\*\\*)", text)
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True  # Bold only
        else:
            paragraph.add_run(part)

def generate_report(findings, filename):
    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cybersecurity expert. Format the report professionally with clear section titles: Executive Summary, Affected Components, Risk Rating, Vulnerabilities Description, Recommendations."},
            {"role": "user", "content": f"Generate a structured vulnerability assessment report based on the following findings:\n{findings}"}
        ]
    )
    report_text = chat_completion.choices[0].message.content

    doc = Document()
    doc.add_heading('Vulnerability Report', 0)
    for section in report_text.split("\n\n"):
        if section.strip():
            if section.strip().endswith(":") or section.strip().startswith("**"):
                heading = doc.add_paragraph()
                run = heading.add_run(section.strip().replace("**", ""))
                run.bold = True
                run.font.color.rgb = RGBColor(0, 112, 192)  # Blue for section titles only
            else:
                para = doc.add_paragraph()
                format_section(para, section.strip())

    output_path = os.path.join(GENERATED_DIR, filename)
    try:
        doc.save(output_path)
    except PermissionError:
        print(f"❌ Cannot write to {output_path}. File is open or locked. Skipping.")
        return None
    return output_path

def main():
    print("🔍 Generating vulnerability reports...\n")
    report_count = 0
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".xlsx")]

    for file in tqdm(files, desc="Processing files"):
        file_path = os.path.join(DATA_DIR, file)
        findings = extract_findings_from_excel(file_path)
        report_file = f"report_{os.path.splitext(file)[0]}.docx"
        generate_report(findings, report_file)
        report_count += 1

    print(f"\n✅ Done. {report_count} report(s) generated in '{GENERATED_DIR}' folder.")

if __name__ == '__main__':
    main()
