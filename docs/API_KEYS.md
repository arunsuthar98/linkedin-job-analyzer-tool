# 🔑 API Keys Guide

This app uses up to 4 API keys. **Only Groq is required** — it's completely free.

---

## 1. 🤖 Groq API Key — FREE (Required for AI features)

**What it powers:** All AI analysis — skill extraction, gap analysis, learning path generation

### How to get it (takes 2 minutes):
1. Go to → **https://console.groq.com**
2. Click **Sign Up** (use Google or Email — no credit card needed)
3. In the dashboard, click **API Keys** in the left menu
4. Click **+ Create API Key**
5. Give it a name: `linkedin-job-analyzer`
6. Copy the key — starts with `gsk_...`

### Add to your `.env` file:
```
GROQ_API_KEY=gsk_your_key_here
```

### Available free models:
| Model | Speed | Best for |
|---|---|---|
| `llama-3.1-8b-instant` | ⚡ Very fast | Default — great for this app |
| `llama-3.3-70b-versatile` | 🐢 Slower | Higher quality analysis |

---

## 2. 📋 JSearch API Key — Free Tier (For live job data)

**What it powers:** Fetches real job postings from LinkedIn, Indeed, Glassdoor

> Without this key, the app uses **demo sample data** (5 mock jobs)

### How to get it:
1. Go to → **https://rapidapi.com/auth/sign-up**
2. Sign up (free account)
3. Go to → **https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch**
4. Click **Pricing** tab → Subscribe to **Basic (Free)** — 200 requests/month
5. Click **Endpoints** tab
6. On the right panel, copy the value of **X-RapidAPI-Key**

### Add to your `.env` file:
```
JSEARCH_API_KEY=your_rapidapi_key_here
```

---

## 3. 📺 YouTube Data API Key — Free (Optional)

**What it powers:** Shows video thumbnails and titles in the Learning Path tab

> Without this key, the app shows **clickable YouTube search links** instead — still fully usable!

### How to get it:
1. Go to → **https://console.cloud.google.com**
2. Sign in with your Google account
3. Click **Select a project** (top left) → **+ New Project**
4. Name: `linkedin-job-analyzer` → **Create**
5. Go to → **https://console.cloud.google.com/apis/library/youtube.googleapis.com**
6. Click **Enable**
7. Go to → **https://console.cloud.google.com/apis/credentials**
8. Click **+ Create Credentials** → **API Key**
9. Copy the key — starts with `AIza...`

### Add to your `.env` file:
```
YOUTUBE_API_KEY=AIza_your_key_here
```

**Free quota:** 10,000 requests/day — more than enough.

---

## 4. 🧠 OpenAI API Key — Paid Optional Alternative

**What it powers:** Same AI features as Groq, but costs ~$0.01–0.05 per analysis

> **Recommendation:** Use Groq instead — it's free and just as capable.

### How to get it:
1. Go to → **https://platform.openai.com/api-keys**
2. Sign up / Log in
3. Click **+ Create new secret key**
4. Copy the key — starts with `sk-...`

### Add to your `.env` file:
```
OPENAI_API_KEY=sk_your_key_here
```

> New accounts get **$5 free credits** — enough for ~500 searches.

---

## Summary

| Key | Required? | Cost | Where to get |
|---|---|---|---|
| Groq | ✅ Yes (for AI) | **FREE** | [console.groq.com](https://console.groq.com) |
| JSearch | 🔶 Optional | Free tier | [rapidapi.com](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) |
| YouTube | 🔶 Optional | Free | [console.cloud.google.com](https://console.cloud.google.com) |
| OpenAI | ❌ Not needed | Paid | [platform.openai.com](https://platform.openai.com/api-keys) |

---

## For Streamlit Cloud Deployment

Add keys in **Streamlit Cloud → App Settings → Secrets**:

```toml
GROQ_API_KEY = "gsk_..."
JSEARCH_API_KEY = "your_rapidapi_key"
YOUTUBE_API_KEY = "AIza..."
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for full deployment instructions.
