# 🚀 Deployment Guide

This guide covers all ways to deploy the LinkedIn Job & Skills Analyzer.

---

## Option 1 — Streamlit Cloud (Recommended, Free)

The easiest way to get a public URL anyone can access.

### Steps:

1. **Fork the repo** on GitHub:
   - Go to → `https://github.com/arunsuthar98/linkedin-job-analyzer-tool`
   - Click **Fork** (top right)

2. **Go to Streamlit Cloud:**
   - → **https://share.streamlit.io**
   - Sign in with your GitHub account

3. **Create new app:**
   - Click **New app**
   - Select your forked repo
   - Branch: `main`
   - Main file path: `app.py`

4. **Add API keys as Secrets:**
   - Click **Advanced settings** → **Secrets**
   - Paste:
   ```toml
   GROQ_API_KEY = "gsk_..."
   JSEARCH_API_KEY = "your_rapidapi_key"
   YOUTUBE_API_KEY = "AIza..."
   ```

5. Click **Deploy** — your app is live in ~60 seconds! 🎉

### Your public URL will look like:
```
https://yourname-linkedin-job-analyzer-tool.streamlit.app
```

---

## Option 2 — Run Locally

### Requirements:
- Python 3.10 or higher
- Git

### Steps:

```bash
# 1. Clone the repo
git clone https://github.com/arunsuthar98/linkedin-job-analyzer-tool.git
cd linkedin-job-analyzer-tool

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys
cp .env.example .env
# Edit .env and add your keys

# 5. Run the app
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## Option 3 — Docker

```dockerfile
# Create a Dockerfile with:
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
```

```bash
docker build -t linkedin-job-analyzer .
docker run -p 8501:8501 --env-file .env linkedin-job-analyzer
```

---

## Updating the App

When new code is pushed to GitHub, Streamlit Cloud **automatically redeploys** within ~30 seconds.

To update locally:
```bash
git pull
pip install -r requirements.txt  # if dependencies changed
streamlit run app.py
```

---

## Environment Variables Reference

| Variable | Default | Description |
|---|---|---|
| `GROQ_API_KEY` | — | Groq AI key (free) |
| `OPENAI_API_KEY` | — | OpenAI key (optional) |
| `JSEARCH_API_KEY` | — | RapidAPI JSearch key |
| `YOUTUBE_API_KEY` | — | YouTube Data API key |
| `GROQ_MODEL` | `llama-3.1-8b-instant` | Groq model to use |
| `OPENAI_MODEL` | `gpt-3.5-turbo` | OpenAI model to use |
| `MAX_JOBS_PER_SEARCH` | `20` | Max job postings per search |
| `CACHE_TTL_SECONDS` | `3600` | Cache duration (1 hour) |

See [API_KEYS.md](API_KEYS.md) for how to get each key.
