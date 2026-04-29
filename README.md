# 💼 LinkedIn Job & Skills Analyzer

An open-source AI agent that searches real job postings, extracts required skills, analyses your personal skill gaps, and generates a personalised learning roadmap — **powered by free AI (Groq)**.

[![CI](https://github.com/arunsuthar98/linkedin-job-analyzer-tool/actions/workflows/ci.yml/badge.svg)](https://github.com/arunsuthar98/linkedin-job-analyzer-tool/actions)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-ff4b4b)
![License](https://img.shields.io/badge/license-MIT-green)
![Free AI](https://img.shields.io/badge/AI-Free%20(Groq)-brightgreen)

🌐 **Live Demo:** https://linkedin-job-analyzer-tool-3b7xatqc3va7qptqxcpxzr.streamlit.app

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Job Role Research** | Search live jobs from LinkedIn, Indeed & Glassdoor |
| 📊 **AI Skills Analysis** | Extract trending skills across dozens of postings |
| 🎯 **Skill Gap Analysis** | Compare your skills vs a job — get a readiness score |
| 📚 **Learning Path** | Phase-based roadmap with YouTube & course links |
| 🆓 **100% Free AI** | Powered by Groq (Llama 3) — no credit card needed |
| 🌐 **Works out of the box** | Pre-configured public demo — no setup required |

---

## 🚀 Try It Now

**No installation needed — just open the link:**

👉 **https://linkedin-job-analyzer-tool-3b7xatqc3va7qptqxcpxzr.streamlit.app**

---

## 📚 Documentation

| Guide | Description |
|---|---|
| [🛠️ Setup Guide](docs/SETUP.md) | Run the app locally on your machine |
| [🔑 API Keys Guide](docs/API_KEYS.md) | How to get free API keys (Groq, JSearch, YouTube) |
| [✨ Features Guide](docs/FEATURES.md) | Full walkthrough of all features and tabs |
| [🚀 Deployment Guide](docs/DEPLOYMENT.md) | Deploy on Streamlit Cloud, Docker, or locally |

---

## ⚡ Quick Start (Local)

```bash
git clone https://github.com/arunsuthar98/linkedin-job-analyzer-tool.git
cd linkedin-job-analyzer-tool
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add your free Groq key
streamlit run app.py
```

See [docs/SETUP.md](docs/SETUP.md) for full instructions.

---

## 🔑 API Keys (All Free)

| Key | Required? | Cost | Get it |
|---|---|---|---|
| **Groq** | ✅ For AI features | **FREE** | [console.groq.com](https://console.groq.com) |
| **JSearch** | 🔶 Optional | Free tier | [rapidapi.com](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) |
| **YouTube** | �� Optional | Free | [console.cloud.google.com](https://console.cloud.google.com) |

See [docs/API_KEYS.md](docs/API_KEYS.md) for step-by-step instructions.

---

## 🏗️ How It Works

```
User enters job role
      ↓
JSearch API → Fetch real job postings (LinkedIn/Indeed/Glassdoor)
      ↓
Groq AI (free) → Extract & rank skills from descriptions
      ↓
User enters their current skills
      ↓
Groq AI → Skill gap analysis + readiness score (0–100)
      ↓
Groq AI → Phase-by-phase learning roadmap
      ↓
YouTube + Coursera/Udemy → Resources for each gap skill
```

---

## 🤝 Contributing

Pull requests welcome! Please keep PRs focused — one feature or fix per PR.

---

## ⚠️ Disclaimer

This tool uses publicly available job posting data via the JSearch API.
It does **not** scrape LinkedIn profiles or violate any Terms of Service.
AI-generated results are estimates — use as a starting point, not authoritative career advice.

---

## 📄 License

MIT — free to use, modify, and distribute.
