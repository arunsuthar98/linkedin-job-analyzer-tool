# 📋 Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.3.0] — Pro Tables, Charts & Resume Coach

### Added
- 📊 **Interactive Plotly charts** in Job Research tab — top hiring companies, top skills, work-mode distribution
- 📋 **Sortable jobs table** with one-click **Apply →** links via `st.column_config.LinkColumn`
- ⬇️ **CSV export** for job search results
- 📈 **KPI metrics row** — Jobs / Companies / Remote / Locations at a glance
- 🎓 **Certifications recommender** (`src/certifications.py`) — curated 30+ industry certs (AWS, Azure, GCP, Data, AI, DevOps, Security, PM, Finance, Software) with level badges, shown in Learning Path tab
- ✍️ **Resume Coach (Tab 6)** — AI-powered tailored resume bullets, LinkedIn headline, LinkedIn About section, missing-keyword detection, likely interview questions
- New AI method: `AIEngine.coach_resume()`

### Changed
- Job Research tab redesigned with KPI cards + charts + sortable table layout
- Tabs renamed to be more concise: 🔍 Job Research · 📊 Skills Trends · 🎯 Skill Gap · 📚 Learning Path · 📄 Resume Match · ✍️ Resume Coach
- `requirements.txt` adds `plotly` and `pandas`

---

## [1.2.0] — UI Polish & Resume Analyzer

### Added
- 📄 **Resume Analyzer (Tab 5)** — upload PDF/DOCX or paste resume text
  - **Mode 1:** AI suggests top 5 matching job roles with % match, strengths & gaps
  - **Mode 2:** Compare resume to a specific job → readiness score, missing skills, suggested headline, training plan
- 🎨 Custom CSS theme — gradient hero header, feature cards, pill tags, animated buttons
- 📜 LICENSE file (MIT — Arun Suthar)
- 🤝 CONTRIBUTING.md — full contributor guide
- 📋 CHANGELOG.md (this file)
- 🔒 PII privacy notice for resume uploads
- 📁 `assets/style.css` — separated styling from logic

### Changed
- App opens with sidebar collapsed for cleaner first impression
- Main page now shows hero banner with feature cards
- README updated with author bio and live demo link

### Security
- Resume uploads capped at 5 MB / 10 pages / 15k chars
- Encrypted PDFs rejected
- All AI prompts use untrusted-input delimiters

---

## [1.1.0] — Free AI (Groq)

### Added
- 🆓 **Groq AI provider support** — Llama 3 free, no credit card needed
- Sidebar status indicator showing which AI provider is active
- `GROQ_API_KEY` and `GROQ_MODEL` env variables

### Changed
- Default AI provider switched from OpenAI to Groq
- Updated all AI calls to use the `active_ai_provider` abstraction
- OpenAI now optional alternative

### Fixed
- Updated default Groq model to `llama-3.1-8b-instant` (older `llama3-8b-8192` decommissioned)

---

## [1.0.0] — Initial Release

### Added
- 🔍 **Tab 1: Job Role Research** — search live jobs via JSearch API
- 📊 **Tab 2: Skills Analysis** — AI extracts trending skills from postings
- 🎯 **Tab 3: Skill Gap Analysis** — compare your skills vs a job
- 📚 **Tab 4: Learning Path** — AI-generated phase-by-phase roadmap
- 🤖 OpenAI integration with structured JSON outputs
- 📋 JSearch (RapidAPI) for live LinkedIn/Indeed/Glassdoor jobs
- 📺 YouTube Data API for video recommendations
- 🎓 Coursera, Udemy, edX, freeCodeCamp deep-link suggestions
- 🔌 Mock data demo mode (works without any API keys)
- 🔑 Skill normalisation & synonym deduplication
- 💾 In-process TTL cache for job search results
- ⬇️ Export learning path as JSON
- 🐳 GitHub Actions CI workflow

---

## Versioning

This project uses [Semantic Versioning](https://semver.org/):
- **Major** — breaking changes
- **Minor** — new features (backward compatible)
- **Patch** — bug fixes
