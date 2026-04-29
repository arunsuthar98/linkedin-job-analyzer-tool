# ✨ Features Guide

A full walkthrough of everything the LinkedIn Job & Skills Analyzer can do.

---

## Tab 1 — 🔍 Job Role Research

**What it does:** Searches for job postings and gives you an overview of the market.

### How to use:
1. Enter a job role (e.g. `Data Scientist`, `Backend Engineer`, `Product Manager`)
2. Optionally add a location (e.g. `London`, `Remote`, `New York`)
3. Check **Remote only** to filter remote jobs
4. Set how many postings to fetch (5–50)
5. Click **Search Jobs**

### What you get:
- 🏢 **Companies hiring** — ranked by number of openings
- 📊 **Quick skill frequency** — most mentioned skills across postings
- 📋 **Job listing** — expandable cards for each posting with full description
- 🎯 **Select any job** to analyse in the Skill Gap tab

### With/without API keys:
| JSearch Key | Result |
|---|---|
| ✅ With key | Real live jobs from LinkedIn, Indeed, Glassdoor |
| ❌ Without key | 5 sample demo jobs |

---

## Tab 2 — 📊 Skills Analysis

**What it does:** AI analyses ALL fetched job postings and extracts trending skills.

### How to use:
1. Run a job search first (Tab 1)
2. Click **Analyse Skills with AI**
3. Wait ~10 seconds

### What you get:
- 🌍 **Role overview** — headline, career level breakdown, market demand
- 🔥 **Trending skills** — what's hot right now
- 🏆 **Top skills ranked** — with percentage frequency and category
- 📂 **Skills by category** — Programming, Cloud, AI/ML, Soft Skills, etc.
- 💡 **AI summary** — prose explanation of the role landscape

---

## Tab 3 — 🎯 Skill Gap Analysis

**What it does:** Compares your skills against a specific job posting.

### How to use:
1. Select a job posting from the dropdown (or click "Analyse This Job" in Tab 1)
2. Enter your current skills (one per line or comma-separated)
3. Optionally add your background (e.g. "2 years as data analyst")
4. Click **Analyse My Skill Gap**

### What you get:
- 🟢🟡🔴 **Readiness score** — 0–100 showing how ready you are
- ✅ **Skills you already have** — matched against the job
- 🚨 **Critical gaps** — must-have skills you're missing
- 💡 **Nice-to-have gaps** — bonus skills that would help
- 💬 **AI coach summary** — honest, encouraging assessment
- 📚 **Button to generate Learning Path** for your gaps

---

## Tab 4 — 📚 Learning Path

**What it does:** Creates a personalised phase-by-phase learning roadmap.

### How to use:
- **Auto:** Click "Generate Learning Path" from Tab 3 (pre-fills your gaps)
- **Manual:** Enter skills directly in this tab

### What you get:
- 🗺️ **Phase-by-phase roadmap** — e.g. Phase 1: Foundations (3 weeks), Phase 2: Core Skills (6 weeks)
- ⏱️ **Total duration estimate** — realistic weeks to job-ready
- 💡 **Study tips** — personalised advice
- 🎥 **YouTube resources** — videos/tutorials for each skill
- 🎓 **Course links** — direct search links to Coursera, Udemy, edX, freeCodeCamp
- ⬇️ **Export as JSON** — download your full roadmap

---

## Demo Mode (No API Keys)

The app is fully usable without any API keys:

| Feature | No keys | With Groq key | With all keys |
|---|---|---|---|
| Job search | ✅ Demo data | ✅ Demo data | ✅ Live data |
| Skill frequency | ✅ From tags | ✅ From tags | ✅ From tags |
| AI skills analysis | ❌ | ✅ | ✅ |
| Skill gap analysis | ❌ | ✅ | ✅ |
| Learning path | ❌ | ✅ | ✅ |
| Video thumbnails | 🔶 Links only | 🔶 Links only | ✅ Thumbnails |

---

## Skill Normalisation

The app automatically normalises skill synonyms so results are accurate:

| You type | Recognised as |
|---|---|
| `sklearn` | `scikit-learn` |
| `pytorch` or `torch` | `PyTorch` |
| `k8s` | `Kubernetes` |
| `ML` | `Machine Learning` |
| `GCP` or `Google Cloud` | `GCP` |

This prevents duplicate counting of the same skill under different names.
