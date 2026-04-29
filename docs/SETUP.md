# 🛠️ Setup Guide

Step-by-step setup for local development.

---

## Prerequisites

- **Python 3.10+** — [download](https://python.org/downloads)
- **Git** — [download](https://git-scm.com)
- A terminal (Command Prompt, PowerShell, or macOS/Linux terminal)

---

## Quick Setup

```bash
# Clone
git clone https://github.com/arunsuthar98/linkedin-job-analyzer-tool.git
cd linkedin-job-analyzer-tool

# Virtual environment
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# Dependencies
pip install -r requirements.txt

# API keys
cp .env.example .env
# Open .env in your editor and fill in your keys

# Run
streamlit run app.py
```

Open **http://localhost:8501** ✅

---

## Getting API Keys

See **[API_KEYS.md](API_KEYS.md)** for detailed instructions on getting each key.

**Quick summary:**
| Key | Where | Cost |
|---|---|---|
| Groq | https://console.groq.com | **FREE** |
| JSearch | https://rapidapi.com | Free tier |
| YouTube | https://console.cloud.google.com | Free |
| OpenAI | https://platform.openai.com | Optional/Paid |

---

## Project Structure

```
linkedin-job-analyzer-tool/
│
├── app.py                        # Main Streamlit app (4 tabs)
│
├── src/
│   ├── config.py                 # API key management
│   ├── job_searcher.py           # JSearch API + mock data
│   ├── skill_analyzer.py         # Skill normalisation & frequency
│   ├── ai_engine.py              # Groq/OpenAI wrapper
│   └── learning_recommender.py   # YouTube + course links
│
├── docs/
│   ├── SETUP.md                  # ← You are here
│   ├── API_KEYS.md               # How to get API keys
│   ├── FEATURES.md               # Full features walkthrough
│   └── DEPLOYMENT.md             # Deployment options
│
├── requirements.txt              # Python dependencies
├── .env.example                  # Template for API keys
└── .gitignore
```

---

## Running in VS Code

1. Open folder: **File → Open Folder** → select `linkedin-job-analyzer-tool`
2. Open terminal: **Ctrl + `**
3. Run:
```bash
source .venv/bin/activate
streamlit run app.py
```
4. VS Code may prompt to open in browser — click **Open**

---

## Troubleshooting

**`ModuleNotFoundError`**
```bash
pip install -r requirements.txt
```

**`streamlit: command not found`**
```bash
# Make sure venv is activated
source .venv/bin/activate
```

**`Error code: model_decommissioned`**
- Update your `.env`: `GROQ_MODEL=llama-3.1-8b-instant`

**App shows demo data instead of real jobs**
- Add your `JSEARCH_API_KEY` to `.env`

**AI features not working**
- Add your `GROQ_API_KEY` to `.env` (free at console.groq.com)
