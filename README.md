# 📄 RapportGen Agent

Un outil Python simple et extensible pour générer automatiquement des rapports de vulnérabilités professionnels à partir de fichiers Excel.
Il utilise l’intelligence de GPT-4 pour transformer des findings bruts en rapports structurés (.docx) prêts à être partagés.

---

## ✨ Fonctionnalités

✅ Génère automatiquement un rapport `.docx` bien structuré pour chaque fichier Excel

✅ Mise en forme avec titres, sous-sections en gras, couleurs pour les sections

✅ Intégration OpenAI GPT-4 (ou GPT-3.5) pour enrichir le contenu

✅ Affichage d’une barre de progression avec `tqdm`

✅ Aucun framework web requis — s’exécute en script CLI simple

---

## 🗂️ Structure du projet

```
rapportgen-agent/
├── genrap.py               # Script principal
├── data/                   # Fichiers Excel à analyser
├── generated_reports/      # Rapports Word générés
├── README.md               # Ce fichier
```

---

## 📦 Dépendances

```bash
pip install pandas openpyxl python-docx openai tqdm
```

---

## ⚙️ Configuration de l’API OpenAI

**Ne jamais publier votre clé dans le code.**

Crée un fichier `.env` :

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Et modifie dans `genrap.py` :

```python
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

---

## ▶️ Utilisation

1. Place tes fichiers `.xlsx` dans le dossier `data/`
2. Lance :

```bash
python genrap.py
```

3. Les fichiers `.docx` seront disponibles dans `generated_reports/`

---

## 📋 Exemple de sections générées

* Executive Summary
* Affected Components
* Risk Rating
* Vulnerabilities Description (avec sous-sections en gras)
* Recommendations

---

## 🧠 Exemple de rendu

> 📷 Tu peux ajouter ici une capture écran d’un rapport Word généré

---

## 🛡️ Auteur

👤 Dr. Sabri ALLANI
🛡️ Expert en cybersécurité & intelligence artificielle

---

## 📜 Licence

MIT License
