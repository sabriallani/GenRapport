# 🔐 VAPT Automated Report Generator

Ce script permet de générer automatiquement des rapports de tests de vulnérabilité (VAPT) à partir de fichiers Excel contenant les résultats de tests. Il utilise GPT-4 pour analyser les logs et déduire automatiquement s’il s’agit d’une **vulnérabilité** ou d’un **comportement résilient**.

---

## 📦 Prérequis

* Python 3.8+
* Une clé API valide OpenAI (`gpt-4` activé)
* Installer les dépendances :

```bash
pip install openai pandas tqdm python-docx
```

---

## 📁 Structure attendue

```
.
├── data/
│   ├── test_cases_logs_1.xlsx
│   └── ...
├── generated_reports/
│   └── vuln_report.docx/json/xlsx/md
├── genrap.py
└── README.md
```

Chaque fichier `.xlsx` doit contenir les colonnes suivantes :

* `Interface`
* `Test Case Description`
* `Test Details`
* `Logs`

---

## 🚀 Utilisation

```bash
python genrap.py <format>
```

**Formats supportés** :

| Format  | Description                                            |
| ------- | ------------------------------------------------------ |
| `docx`  | Rapport Word lisible par humains                       |
| `excel` | Fichier `.xlsx` tabulaire (interne/automatisation)     |
| `json`  | Fichier `.json` pour intégration dans SIEM/API         |
| `md`    | Rapport Markdown (idéal pour GitHub Pages, Docs, etc.) |

---

### Exemple

```bash
python genrap.py docx
python genrap.py json
python genrap.py md
```

---

## 🧠 Fonctionnement

1. Le script lit tous les fichiers `.xlsx` du dossier `data/`
2. Il envoie chaque log à GPT-4 pour classification : `VULNERABILITY` ou `SUCCESS`
3. Si une vulnérabilité est détectée, GPT-4 génère un résumé détaillé : CVSS, CWE, description, risques, etc.
4. Tous les résultats sont rassemblés dans un fichier de sortie du format demandé.

---

## 📌 Exemple de sortie Markdown

```markdown
## 3.1 Test GPS Spoofing
- **Result**: VULNERABILITY
- **CVSS**: 7.5
- **Risk level**: High
- **CWE/CVE reference**: CWE-287
...

---

## 3.2 Test Signal Jamming
- **Result**: SUCCESS
- **Message**: The system is resilient. No vulnerability found.
```

---

## 🔗 Auteur

Projet automatisé pour les experts cybersécurité / pentesters.
