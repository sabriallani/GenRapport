# 🔐 Automated VAPT Report Generator

> **VAPT** : *Vulnerability Assessment and Penetration Testing* – c'est une méthode d'audit de sécurité permettant d'identifier, analyser et rapporter les failles de sécurité potentielles dans une application, un système ou un réseau.

Ce projet permet de générer automatiquement des rapports de tests de vulnérabilité (VAPT) à partir de fichiers Excel contenant des logs d’exécution de cas de test. L’analyse est effectuée automatiquement par un LLM (local ou distant) pour déterminer s’il s’agit d’un **succès (résilience)** ou d’une **vulnérabilité**, et générer un rapport formaté.

---

## 📦 Prérequis

* Python 3.8+
* Une clé API OpenAI (si vous utilisez le mode distant)
* Dépendances :

```bash
pip install openai pandas tqdm python-docx
```

---

## ⚙️ Modes de fonctionnement

### 1. 🔗 Mode distant (via OpenAI)

Utilise le fichier `genrap.py` avec un appel à l’API OpenAI (gpt-4 ou gpt-3.5).
👉 **Configurer la clé API dans `genrap.py`** :

```python
client = OpenAI(api_key="sk-votre_cle_openai")
```

Changer le modèle si nécessaire :

```python
model="gpt-3.5-turbo"  # ou "gpt-4" si disponible
```

Lancer la génération :

```bash
python genrap.py docx
```

---

### 2. 🧠 Mode local (sans Internet)

Utilise un modèle local optimisé type Mistral via `localgen.py`.
⚠️ Requiert `llama-cpp-python` et un modèle `.gguf` tel que :

```
models/
└── openhermes-2.5-mistral-7b.Q5_K_M.gguf
```

🔗 Télécharger le modèle depuis Hugging Face : [TheBloke/OpenHermes-2.5-Mistral-7B-GGUF](https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF)

#### 📦 Dépendances (mode local)

```bash
pip install llama-cpp-python pandas tqdm
```

#### ⚙️ Configuration minimale recommandée

* CPU 6+ cores ou GPU compatible (CUDA/Metal selon version `llama-cpp`)
* RAM ≥ 8 Go
* Plus le modèle est grand (7B, 13B), plus l’analyse sera précise mais lente.
* Modèle recommandé : `openhermes-2.5-mistral-7b.Q5_K_M.gguf`

Lancer la génération :

```bash
python localgen.py md
```

---

## 📁 Structure attendue

```
.
├── data/
│   ├── test_cases_logs_failure 1.xlsx
│   ├── test_cases_logs_success 1.xlsx
├── models/
│   └── openhermes-2.5-mistral-7b.Q5_K_M.gguf
├── generated_reports/
│   └── vuln_report.docx/json/xlsx/md
├── genrap.py          # Script OpenAI distant
├── localgen.py        # Script modèle local
└── README.md
```

Chaque fichier Excel doit contenir les colonnes suivantes :

* `Interface`
* `Test Case Description`
* `Test Details`
* `Logs`

---

## 🚀 Utilisation des formats

```bash
python genrap.py <format>
python localgen.py <format>
```

**Formats supportés** :

| Format  | Description                                      |
| ------- | ------------------------------------------------ |
| `docx`  | Rapport Word lisible                             |
| `excel` | Format `.xlsx` pour intégration automatisée      |
| `json`  | Format `.json` pour SIEM ou API                  |
| `md`    | Rapport Markdown pour documentation GitHub, etc. |

---

## 📌 Exemple de sortie Markdown

```markdown
## 3.1 Test GPS Spoofing
- **Result**: VULNERABILITY
- **CVSS**: 7.5
- **Risk level**: High
- **CWE/CVE reference**: CWE-287
...

## 3.2 Test Signal Jamming
- **Result**: SUCCESS
- **Message**: The system is resilient. No vulnerability found.
```

---

## 📌 Exemple de sortie JSON

```json
[
  {
    "test_id": "3.1",
    "name": "Test GPS Spoofing",
    "result": "VULNERABILITY",
    "cvss": 7.5,
    "risk_level": "High",
    "cwe": "CWE-287",
    "description": "This vulnerability allows GPS spoofing...",
    "recommendation": "Use encrypted GPS receivers."
  },
  {
    "test_id": "3.2",
    "name": "Test Signal Jamming",
    "result": "SUCCESS",
    "message": "The system is resilient. No vulnerability found."
  }
]
```

---

## 🧠 Fonctionnement

1. Lecture automatique de tous les fichiers `.xlsx` dans `data/`
2. Analyse sémantique des logs (succès ou vulnérabilité)
3. En cas de vulnérabilité :

   * Génération des éléments : CVSS, CWE, description, risques, complexité, etc.
4. Génération du fichier final dans `generated_reports/`

---

## 🧑‍💼 Auteur

Automatisation proposée pour les experts cybersécurité et les équipes de test VAPT.

---
