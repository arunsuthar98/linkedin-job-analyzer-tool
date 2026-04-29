# 💼 LinkedIn Job & Skills Analyzer

An open-source AI agent that searches real job postings, extracts required skills, analyses your personal skill gaps, and generates a personalised learning roadmap — all powered by OpenAI.

[![CI](https://github.com/arunsuthar98/linkedin-job-analyzer/actions/workflows/ci.yml/badge.svg)](https://github.com/arunsuthar98/linkedin-job-analyzer/actions)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-ff4b4b)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Job Role Research** | Search live job postings aggregated from LinkedIn, Indeed & Glassdoor |
| 📊 **AI Skills Analysis** | Extract trending skills and categories from dozens of postings at once |
| 🎯 **Skill Gap Analysis** | Compare your skills vs a specific job posting and get a readiness score |
| 📚 **Learning Path** | AI-generated phase-based roadmap with YouTube videos and course links |
| 🔒 **Privacy-first** | API keys never leave your browser session; no account required |
| 🌐 **Demo mode** | Works without any API keys using built-in sample data |

---

## 🚀 Quick Start (Local)

### 1. Clone the repository

```bash
git clone https://github.com/arunsuthar98/linkedin-job-analyzer.git
cd linkedin-job-analyzer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

```bash
cp .env.example .env
# Edit .env and add your API keys (see the API Keys section below)
```

### 5. Run the app

```bash
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## 🔑 API Keys

All keys are **optional** — the app degrades gracefully without them.

| Key | Required? | How to get | What it unlocks |
|---|---|---|---|
| **OpenAI** | ✅ Recommended | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) | All AI analysis features |
| **JSearch (RapidAPI)** | 🔶 Optional | [rapidapi.com/.../jsearch](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) | Live job postings (free tier: 200 req/mo) |
| **YouTube Data API** | 🔶 Optional | [console.cloud.google.com](https://console.cloud.google.com/apis/library/youtube.googleapis.com) | Embedded video previews (free quota) |

**Without any keys:** the app runs in demo mode with sample job postings and generates AI-powered analysis once you add your OpenAI key.

You can also enter keys directly in the **sidebar** without creating a `.env` file — they are stored only in your browser session.

---

## ☁️ Deploy on Streamlit Cloud (Free)

1. Fork this repo to your GitHub account.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app** → select your fork → set **Main file path** to `app.py`.
4. In **Advanced settings → Secrets**, add:

```toml
OPENAI_API_KEY = "sk-..."
JSEARCH_API_KEY = "your_rapidapi_key"
YOUTUBE_API_KEY = "AIza..."
```

5. Click **Deploy** — your public URL is live in ~60 seconds.

---

## 🐳 Docker (Optional)

```bash
docker build -t linkedin-job-analyzer .
docker run -p 8501:8501 --env-file .env linkedin-job-analyzer
```

> A `Dockerfile` is not included by default. Create one with:
> ```dockerfile
> FROM python:3.11-slim
> WORKDIR /app
> COPY requirements.txt .
> RUN pip install -r requirements.txt
> COPY . .
> EXPOSE 8501
> CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
> ```

---

## 🏗️ Project Structure

```
linkedin-job-analyzer/
├── app.py                       # Streamlit UI (4 tabs)
├── src/
│   ├── config.py                # API key management (.env + UI)
│   ├── job_searcher.py          # JSearch API client + mock data
│   ├── skill_analyzer.py        # Skill normalisation & frequency counting
│   ├── ai_engine.py             # OpenAI wrapper (structured JSON output)
│   └── learning_recommender.py  # YouTube API + Coursera/Udemy deep links
├── requirements.txt
├── .env.example                 # Template — copy to .env
├── .gitignore
└── .github/
    └── workflows/ci.yml         # GitHub Actions CI
```

---

## 🛠️ How It Works

```
User enters job role
        │
        ▼
JSearch API ──→ Fetch job postings (LinkedIn/Indeed/Glassdoor)
        │
        ▼
OpenAI GPT ──→ Extract & normalise skills from descriptions
        │
        ▼
User enters current skills
        │
        ▼
OpenAI GPT ──→ Skill gap analysis (matched / critical / nice-to-have)
        │
        ▼
OpenAI GPT ──→ Phase-by-phase learning roadmap
        │
        ▼
YouTube API / Coursera / Udemy ──→ Resources for each gap skill
```

**Key technical decisions:**
- **No LinkedIn scraping** — uses JSearch which aggregates public job-board pages legally.
- **Structured JSON output** from OpenAI prevents hallucinations and makes responses machine-parseable.
- **Skill synonym normalisation** (e.g. `sklearn` → `scikit-learn`) ensures accurate frequency counting.
- **In-process TTL cache** avoids redundant API calls within a session.
- **Dual secrets model** — `.env` for local, sidebar input for hosted demos.

---

## 🤝 Contributing

Pull requests are welcome!

1. Fork → create feature branch → commit → open PR.
2. Please include a short description of what your PR changes and why.
3. Keep PRs focused — one feature/fix per PR.

---

## 📄 License

MIT — free to use, modify, and distribute.

---

## ⚠️ Disclaimer

This tool searches publicly available job posting data and uses AI to analyse it.
It does **not** scrape LinkedIn user profiles or violate any platform's Terms of Service.
Results are AI-generated estimates and should be used as a starting point, not as authoritative career advice.
