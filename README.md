<div align="center">

# 💼 LinkedIn Job & Skills Analyzer

### Your AI-powered career copilot — discover jobs, close skill gaps, build your learning roadmap.

[![CI](https://github.com/arunsuthar98/linkedin-job-analyzer-tool/actions/workflows/ci.yml/badge.svg)](https://github.com/arunsuthar98/linkedin-job-analyzer-tool/actions)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-ff4b4b)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Free AI](https://img.shields.io/badge/AI-Free%20(Groq)-brightgreen)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

### 🌐 [**Try the Live Demo →**](https://linkedin-job-analyzer-tool-3b7xatqc3va7qptqxcpxzr.streamlit.app)

</div>

---

## ✨ What it does

| Feature | Description |
|---|---|
| 🔍 **Job Role Research** | Search live jobs from LinkedIn, Indeed & Glassdoor |
| 📊 **AI Skills Analysis** | Extract trending skills across dozens of postings |
| 🎯 **Skill Gap Analysis** | Compare your skills vs a job — get a readiness score |
| 📚 **Learning Path** | Phase-based roadmap with YouTube & course links |
| 📄 **Resume Analyzer** | Upload your resume → AI suggests best-fit roles + training plan |
| 🆓 **100% Free AI** | Powered by Groq (Llama 3) — no credit card needed |

---

## 🚀 Try It Now (No Install)

👉 **https://linkedin-job-analyzer-tool-3b7xatqc3va7qptqxcpxzr.streamlit.app**

The hosted demo is pre-configured with API keys — just open and use!

---

## 📚 Documentation

| Guide | Description |
|---|---|
| 🛠️ [SETUP.md](docs/SETUP.md) | Install and run locally |
| 🔑 [API_KEYS.md](docs/API_KEYS.md) | How to get the free API keys |
| ✨ [FEATURES.md](docs/FEATURES.md) | Full walkthrough of every feature |
| 🚀 [DEPLOYMENT.md](docs/DEPLOYMENT.md) | Deploy on Streamlit Cloud, Docker, or self-host |
| 🤝 [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| 📋 [CHANGELOG.md](CHANGELOG.md) | Version history |

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

→ Open **http://localhost:8501** ✅

---

## 🔑 API Keys (All Free)

| Key | Required? | Cost | Get it |
|---|---|---|---|
| **Groq** | ✅ For AI | **FREE** | [console.groq.com](https://console.groq.com) |
| **JSearch** | 🔶 Optional | Free tier | [rapidapi.com](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) |
| **YouTube** | 🔶 Optional | Free | [console.cloud.google.com](https://console.cloud.google.com) |

See [docs/API_KEYS.md](docs/API_KEYS.md) for step-by-step instructions.

---

## 🏗️ How It Works

```
                 ┌────────────────────────────┐
                 │   👤 User                  │
                 │   (job role / resume)      │
                 └─────────────┬──────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
  ┌──────────┐          ┌──────────────┐       ┌──────────────┐
  │ JSearch  │          │ Groq AI      │       │ PDF / DOCX   │
  │  API     │          │ (Llama 3)    │       │  Parser      │
  └─────┬────┘          └──────┬───────┘       └──────┬───────┘
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               ▼
                ┌─────────────────────────────┐
                │  Streamlit GUI (5 tabs)     │
                │  Search · Analyse · Match · │
                │  Roadmap · Resume           │
                └─────────────┬───────────────┘
                              ▼
                ┌─────────────────────────────┐
                │  YouTube + Coursera + Udemy │
                │  → Training Resources       │
                └─────────────────────────────┘
```

---

## 🏗️ Project Structure

```
linkedin-job-analyzer-tool/
├── app.py                       # Main Streamlit app (5 tabs)
├── src/
│   ├── config.py                # API key management
│   ├── job_searcher.py          # JSearch API + mock data
│   ├── skill_analyzer.py        # Skill normalisation
│   ├── ai_engine.py             # Groq + OpenAI wrapper
│   ├── learning_recommender.py  # YouTube + course links
│   └── resume_parser.py         # PDF/DOCX parsing
├── assets/
│   └── style.css                # Custom theme
├── docs/                        # Full documentation
├── .streamlit/config.toml       # Streamlit theme
├── requirements.txt
├── .env.example
├── LICENSE
├── CONTRIBUTING.md
└── CHANGELOG.md
```

---

## 🤝 Contributing

Pull requests are very welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

Star ⭐ the repo if you find it useful!

---

## 👤 Author

**Arun Suthar**
- 🌐 GitHub: [@arunsuthar98](https://github.com/arunsuthar98)
- 📧 Email: arunsuthar98@gmail.com
- 💼 Built with ❤️ for everyone navigating their tech career journey

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, distribute, and even sell this software, as long as you include the original copyright notice.

---

## 🙏 Acknowledgements

- 🤖 [Groq](https://console.groq.com) — for blazing-fast free AI inference
- 📋 [JSearch by Letscrape](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) — for aggregated job data
- 🎨 [Streamlit](https://streamlit.io) — for making beautiful apps simple
- 📺 [YouTube Data API](https://developers.google.com/youtube/v3) — for video discovery
- ❤️ Everyone who stars, contributes, or shares this project

---

## ⚠️ Disclaimer

This tool uses publicly available job posting data via the JSearch API.
It does **not** scrape LinkedIn user profiles or violate any Terms of Service.
AI-generated results are estimates — use as a starting point, not authoritative career advice.

---

<div align="center">

**Made with 💙 by [Arun Suthar](https://github.com/arunsuthar98)** · If this helped you, please ⭐ star the repo!

</div>
