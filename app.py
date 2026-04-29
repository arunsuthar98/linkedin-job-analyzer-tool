"""LinkedIn Job & Skills Analyzer — main Streamlit application.

Tabs:
  1. 🔍 Job Role Research   — search jobs, view companies & skills
  2. 📊 Skills Analysis     — AI-generated skill trends
  3. 🎯 Skill Gap Analysis  — compare your skills against a job posting
  4. 📚 Learning Path       — personalised recommendations
"""
from __future__ import annotations

import streamlit as st

from src.ai_engine import AIEngine
from src.config import Config
from src.job_searcher import JobPosting, JobSearcher
from src.learning_recommender import LearningRecommender
from src.skill_analyzer import frequency_map, normalize_skills

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="LinkedIn Job & Skills Analyzer",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Session-state defaults
# ---------------------------------------------------------------------------

DEFAULTS = {
    "postings": [],
    "is_mock": True,
    "skills_analysis": None,
    "role_overview": None,
    "selected_job_idx": None,
    "gap_analysis": None,
    "learning_path": None,
    "user_skills": [],
    "search_done": False,
    "job_role": "",
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ---------------------------------------------------------------------------
# Sidebar — API keys
# ---------------------------------------------------------------------------

with st.sidebar:
    st.title("⚙️ Configuration")
    st.success("✅ App is pre-configured and ready to use!")
    st.markdown(
        "The app works out of the box with default API keys.  \n"
        "You can optionally enter **your own keys** below to use your personal quota."
    )
    st.divider()

    cfg = Config()  # loads from .env / Streamlit secrets if present

    with st.expander("🔑 Use my own API keys (optional)"):
        groq_key_input = st.text_input(
            "Groq API Key (FREE)",
            value="",
            type="password",
            placeholder="gsk_... (get free at console.groq.com)",
        )
        openai_key_input = st.text_input(
            "OpenAI API Key (optional)",
            value="",
            type="password",
            placeholder="sk-...",
        )
        jsearch_key_input = st.text_input(
            "JSearch API Key (RapidAPI)",
            value="",
            type="password",
            placeholder="Your RapidAPI key",
        )
        youtube_key_input = st.text_input(
            "YouTube Data API Key",
            value="",
            type="password",
            placeholder="AIza...",
        )
        cfg.update_from_ui(
            groq_key=groq_key_input or None,
            openai_key=openai_key_input or None,
            jsearch_key=jsearch_key_input or None,
            youtube_key=youtube_key_input or None,
        )

    st.divider()
    st.markdown("**Status**")
    if cfg.has_groq:
        st.markdown("✅ Groq AI — active (FREE)")
    elif cfg.has_openai:
        st.markdown("✅ OpenAI — active")
    else:
        st.markdown("⚠️ No AI key found")
    st.markdown(f"{'✅' if cfg.has_jsearch else '🔶'} JSearch — {'live data' if cfg.has_jsearch else 'demo mode'}")
    st.markdown(f"{'✅' if cfg.has_youtube else '🔶'} YouTube — {'connected' if cfg.has_youtube else 'URL fallback'}")

    st.divider()
    st.caption(
        "💡 **Get your own free keys:**\n"
        "- [Groq (FREE)](https://console.groq.com)\n"
        "- [RapidAPI / JSearch](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch)\n"
        "- [YouTube Data API](https://console.cloud.google.com/apis/library/youtube.googleapis.com)\n"
        "- [OpenAI](https://platform.openai.com/api-keys)"
    )

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

st.title("💼 LinkedIn Job & Skills Analyzer")
st.markdown(
    "Search real job postings, identify required skills, analyse your skill gaps, "
    "and get a personalised learning roadmap — all powered by AI."
)

if not cfg.has_any_ai:
    st.warning(
        "⚠️ No AI key configured. If you're running locally, add a free Groq key to your `.env` file.  \n"
        "See [docs/API_KEYS.md](docs/API_KEYS.md) for instructions."
    )

# ---------------------------------------------------------------------------
# Tabs
# ---------------------------------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    ["🔍 Job Role Research", "📊 Skills Analysis", "🎯 Skill Gap Analysis", "📚 Learning Path"]
)

# ============================================================
# TAB 1 — Job Role Research
# ============================================================

with tab1:
    st.header("🔍 Job Role Research")
    st.markdown("Search for jobs and discover which companies are hiring and what skills they need.")

    col1, col2, col3 = st.columns([3, 2, 1])
    with col1:
        job_role = st.text_input(
            "Job Role",
            value=st.session_state.job_role or "",
            placeholder="e.g. Data Scientist, Backend Engineer, Product Manager",
        )
    with col2:
        location = st.text_input("Location (optional)", placeholder="e.g. London, Remote, New York")
    with col3:
        remote_only = st.checkbox("Remote only")

    max_results = st.slider("Max job postings to fetch", 5, 50, 20, step=5)

    search_clicked = st.button("🔍 Search Jobs", type="primary", use_container_width=True)

    if search_clicked and job_role.strip():
        st.session_state.job_role = job_role.strip()
        # Reset downstream state
        for key in ["postings", "skills_analysis", "role_overview",
                    "selected_job_idx", "gap_analysis", "learning_path", "search_done"]:
            st.session_state[key] = DEFAULTS[key]

        searcher = JobSearcher(
            api_key=cfg.jsearch_api_key,
            cache_ttl=cfg.cache_ttl_seconds,
        )
        with st.spinner("Searching job postings…"):
            try:
                postings, is_mock = searcher.search(
                    job_role=job_role.strip(),
                    location=location,
                    remote_only=remote_only,
                    max_results=max_results,
                )
                st.session_state.postings = postings
                st.session_state.is_mock = is_mock
                st.session_state.search_done = True
            except RuntimeError as e:
                st.error(f"Search failed: {e}")

    if st.session_state.search_done:
        postings: list[JobPosting] = st.session_state.postings
        is_mock: bool = st.session_state.is_mock

        if is_mock:
            st.info(
                "🔶 **Demo mode** — showing sample data.  \n"
                "Add a JSearch API key in the sidebar to fetch live postings."
            )

        if not postings:
            st.warning("No job postings found. Try a different role or location.")
        else:
            st.success(f"Found **{len(postings)}** job postings for **{st.session_state.job_role}**")

            # Companies
            searcher_tmp = JobSearcher(api_key=None)
            companies = searcher_tmp.top_companies(postings)

            col_a, col_b = st.columns(2)
            with col_a:
                st.subheader("🏢 Companies Hiring")
                for company, count in companies[:10]:
                    st.markdown(f"- **{company}** — {count} posting{'s' if count > 1 else ''}")

            with col_b:
                st.subheader("📌 Quick Skill Frequency")
                all_skills = [p.skills_raw for p in postings if p.skills_raw]
                if all_skills:
                    freq = frequency_map(all_skills)
                    for skill, count in list(freq.items())[:10]:
                        pct = int(count / len(postings) * 100)
                        st.markdown(f"- **{skill}** — {pct}% of postings")
                else:
                    st.caption("Skill tags not available from this data source — use the Skills Analysis tab.")

            # Job listing
            st.subheader("📋 Job Postings")
            for i, p in enumerate(postings):
                remote_badge = " 🌐 Remote" if p.is_remote else ""
                with st.expander(f"{p.title} — {p.company} ({p.location}){remote_badge}"):
                    st.markdown(f"**Source:** {p.source}")
                    if p.date_posted:
                        st.markdown(f"**Posted:** {p.date_posted[:10]}")
                    if p.employment_type:
                        st.markdown(f"**Type:** {p.employment_type}")
                    st.markdown("**Description:**")
                    st.text(p.description[:800] + ("…" if len(p.description) > 800 else ""))
                    if p.url:
                        st.link_button("View Full Posting", p.url)
                    if st.button(f"🎯 Analyse This Job", key=f"select_{i}"):
                        st.session_state.selected_job_idx = i
                        st.session_state.gap_analysis = None
                        st.success(f"Selected: **{p.title}** at {p.company}. Go to the Skill Gap Analysis tab.")

# ============================================================
# TAB 2 — Skills Analysis
# ============================================================

with tab2:
    st.header("📊 Skills Analysis")
    st.markdown("AI-powered analysis of skills and trends across all fetched job postings.")

    if not st.session_state.search_done or not st.session_state.postings:
        st.info("👆 Run a job search in the **Job Role Research** tab first.")
    else:
        postings = st.session_state.postings
        job_role = st.session_state.job_role

        if st.button("🤖 Analyse Skills with AI", type="primary", disabled=not cfg.has_any_ai):
            if not cfg.has_any_ai:
                st.warning("Add a free Groq API key in the sidebar.")
            else:
                descriptions = [p.description for p in postings if p.description]
                ai = AIEngine(api_key=cfg.active_ai_key, provider=cfg.active_ai_provider, model=cfg.active_model)

                with st.spinner("Analysing skills across all job postings…"):
                    try:
                        analysis = ai.extract_skills_from_postings(job_role, descriptions)
                        st.session_state.skills_analysis = analysis
                    except Exception as e:
                        st.error(f"AI analysis failed: {e}")

                with st.spinner("Generating role overview…"):
                    try:
                        overview = ai.analyze_role_overview(job_role, analysis)
                        st.session_state.role_overview = overview
                    except Exception as e:
                        st.warning(f"Role overview unavailable: {e}")

        if not cfg.has_any_ai:
            st.warning("Add your free Groq API key to enable AI analysis.")

        analysis = st.session_state.skills_analysis
        overview = st.session_state.role_overview

        if overview:
            st.subheader("🌍 Role Overview")
            st.markdown(f"**{overview.get('headline', '')}**")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Career levels:**")
                st.write(overview.get("career_level_breakdown", ""))
                st.markdown("**Market demand:**")
                st.write(overview.get("market_demand", ""))
            with col2:
                trending = overview.get("trending_skills", [])
                if trending:
                    st.markdown("**Trending skills right now:**")
                    for s in trending:
                        st.markdown(f"- 🔥 {s}")

        if analysis:
            st.subheader("🏆 Top Skills Required")
            top_skills = analysis.get("top_skills", [])
            if top_skills:
                for skill_info in top_skills[:15]:
                    skill = skill_info.get("skill", "")
                    freq = skill_info.get("frequency_pct", 0)
                    cat = skill_info.get("category", "")
                    st.progress(freq / 100, text=f"**{skill}** ({cat}) — {freq}%")

            categories = analysis.get("categories", {})
            if categories:
                st.subheader("📂 Skills by Category")
                cols = st.columns(min(len(categories), 3))
                for idx, (cat, skills) in enumerate(categories.items()):
                    with cols[idx % 3]:
                        st.markdown(f"**{cat}**")
                        for s in skills:
                            st.markdown(f"- {s}")

            summary = analysis.get("summary", "")
            if summary:
                st.subheader("💡 AI Summary")
                st.info(summary)

        elif not analysis and st.session_state.search_done:
            # Show basic frequency without AI
            all_skills = [p.skills_raw for p in postings if p.skills_raw]
            if all_skills:
                st.subheader("📊 Skill Frequency (from posting tags)")
                freq = frequency_map(all_skills)
                for skill, count in list(freq.items())[:15]:
                    pct = int(count / len(postings) * 100)
                    st.progress(pct / 100, text=f"**{skill}** — {pct}%")

# ============================================================
# TAB 3 — Skill Gap Analysis
# ============================================================

with tab3:
    st.header("🎯 Skill Gap Analysis")
    st.markdown("Compare your current skills against a specific job posting.")

    if not st.session_state.search_done or not st.session_state.postings:
        st.info("👆 Run a job search first, then select a job posting to analyse.")
    else:
        postings = st.session_state.postings
        job_role = st.session_state.job_role

        # Job selector
        posting_options = {
            f"{p.title} — {p.company}": i for i, p in enumerate(postings)
        }
        selected_label = st.selectbox(
            "Select a job posting to analyse",
            options=list(posting_options.keys()),
            index=st.session_state.selected_job_idx or 0,
        )
        selected_idx = posting_options[selected_label]
        selected_job = postings[selected_idx]

        st.markdown(f"**Role:** {selected_job.title}  \n**Company:** {selected_job.company}  \n**Location:** {selected_job.location}")

        # User skills input
        st.subheader("🛠️ Your Current Skills")
        skills_text = st.text_area(
            "Enter your skills (one per line or comma-separated)",
            value="\n".join(st.session_state.user_skills) if st.session_state.user_skills else "",
            placeholder="Python\nSQL\nMachine Learning\nDocker",
            height=150,
        )

        background = st.text_input(
            "Your background (optional)",
            placeholder="e.g. 2 years as data analyst, BSc in Computer Science",
        )

        analyse_btn = st.button(
            "🤖 Analyse My Skill Gap",
            type="primary",
            disabled=not cfg.has_any_ai,
        )

        if not cfg.has_any_ai:
            st.warning("Add your free Groq API key to enable skill gap analysis.")

        if analyse_btn:
            if not skills_text.strip():
                st.warning("Please enter your skills first.")
            elif not cfg.has_any_ai:
                st.warning("Add a free Groq API key in the sidebar.")
            else:
                # Parse skills from textarea
                raw_skills = [
                    s.strip()
                    for line in skills_text.replace(",", "\n").splitlines()
                    for s in [line.strip()]
                    if s.strip()
                ]
                user_skills = normalize_skills(raw_skills)
                st.session_state.user_skills = user_skills

                ai = AIEngine(api_key=cfg.active_ai_key, provider=cfg.active_ai_provider, model=cfg.active_model)
                with st.spinner("Analysing your skill gap…"):
                    try:
                        gap = ai.perform_skill_gap_analysis(
                            job_role=selected_job.title,
                            job_description=selected_job.description,
                            user_skills=user_skills,
                        )
                        st.session_state.gap_analysis = gap
                        st.session_state.selected_job_idx = selected_idx
                    except Exception as e:
                        st.error(f"Analysis failed: {e}")

        gap = st.session_state.gap_analysis
        if gap:
            score = gap.get("readiness_score", 0)
            colour = "🟢" if score >= 70 else "🟡" if score >= 40 else "🔴"

            st.divider()
            st.subheader(f"{colour} Readiness Score: {score}/100")
            st.progress(score / 100)

            col1, col2, col3 = st.columns(3)
            with col1:
                matched = gap.get("matched_skills", [])
                st.markdown(f"**✅ Skills You Have ({len(matched)})**")
                for s in matched:
                    st.markdown(f"- ✅ {s}")
            with col2:
                critical = gap.get("missing_critical", [])
                st.markdown(f"**🚨 Critical Gaps ({len(critical)})**")
                for s in critical:
                    st.markdown(f"- 🚨 {s}")
            with col3:
                nice = gap.get("missing_nice_to_have", [])
                st.markdown(f"**💡 Nice-to-Have ({len(nice)})**")
                for s in nice:
                    st.markdown(f"- 💡 {s}")

            summary = gap.get("summary", "")
            if summary:
                st.info(f"💬 **AI Coach:** {summary}")

            all_missing = gap.get("missing_critical", []) + gap.get("missing_nice_to_have", [])
            if all_missing:
                if st.button("📚 Generate Learning Path for These Gaps", type="primary"):
                    st.session_state.learning_path = None
                    st.session_state["_pending_learning"] = {
                        "skills": all_missing,
                        "background": background,
                    }
                    st.success("Go to the **Learning Path** tab to see your roadmap!")

# ============================================================
# TAB 4 — Learning Path
# ============================================================

with tab4:
    st.header("📚 Learning Path")
    st.markdown("A personalised roadmap to acquire the skills you need for your target role.")

    pending = st.session_state.get("_pending_learning")
    gap = st.session_state.gap_analysis
    job_role = st.session_state.job_role

    # Allow manual skill entry if arriving directly
    if not gap and not pending:
        st.info("Complete the **Skill Gap Analysis** tab first to auto-populate your missing skills, or enter them manually below.")

    # Manual entry fallback
    manual_skills = st.text_area(
        "Skills to learn (one per line, or filled automatically from Skill Gap Analysis)",
        value="\n".join(pending["skills"] if pending else (
            (gap.get("missing_critical", []) + gap.get("missing_nice_to_have", [])) if gap else []
        )),
        height=120,
    )
    manual_background = st.text_input(
        "Your background",
        value=pending.get("background", "") if pending else "",
        placeholder="e.g. 1 year of Python experience, transitioning from data analyst",
    )
    manual_role = st.text_input("Target job role", value=job_role or "", placeholder="Data Scientist")

    generate_btn = st.button(
        "🗺️ Generate Learning Path",
        type="primary",
        disabled=not cfg.has_any_ai,
    )
    if not cfg.has_any_ai:
        st.warning("Add your free Groq API key to generate a learning path.")

    if generate_btn:
        skills_to_learn = [
            s.strip()
            for line in manual_skills.splitlines()
            for s in [line.strip()]
            if s.strip()
        ]
        target_role = manual_role.strip() or job_role or "target role"

        if not skills_to_learn:
            st.warning("Please enter at least one skill to learn.")
        elif not cfg.has_any_ai:
            st.warning("Add a free Groq API key in the sidebar.")
        else:
            ai = AIEngine(api_key=cfg.active_ai_key, provider=cfg.active_ai_provider, model=cfg.active_model)
            with st.spinner("Generating your personalised learning path…"):
                try:
                    path = ai.generate_learning_path(
                        job_role=target_role,
                        missing_skills=skills_to_learn,
                        user_background=manual_background,
                    )
                    st.session_state.learning_path = {
                        "path": path,
                        "skills": skills_to_learn,
                        "role": target_role,
                    }
                    st.session_state["_pending_learning"] = None
                except Exception as e:
                    st.error(f"Could not generate learning path: {e}")

    lp_data = st.session_state.learning_path
    if lp_data:
        path = lp_data["path"]
        skills = lp_data["skills"]
        role = lp_data["role"]

        total_weeks = path.get("total_duration_weeks", "?")
        st.success(f"🗺️ Your learning roadmap — estimated **{total_weeks} weeks** to job-ready for **{role}**")

        phases = path.get("phases", [])
        for phase in phases:
            with st.expander(
                f"Phase {phase.get('phase', '')}: {phase.get('title', '')} "
                f"({phase.get('duration_weeks', '?')} weeks)",
                expanded=phase.get("phase", 1) == 1,
            ):
                st.markdown(phase.get("description", ""))
                phase_skills = phase.get("skills", [])
                if phase_skills:
                    st.markdown("**Skills covered:** " + ", ".join(phase_skills))

        tips = path.get("tips", [])
        if tips:
            st.subheader("💡 Study Tips")
            for tip in tips:
                st.markdown(f"- {tip}")

        # Learning resources
        st.subheader("🎥 Learning Resources")
        st.markdown("Find tutorials and courses for each skill:")

        recommender = LearningRecommender(youtube_api_key=cfg.youtube_api_key)
        search_queries = path.get("search_queries", {})

        with st.spinner("Fetching learning resources…"):
            resources_list = recommender.get_resources_for_skills(
                skills=skills[:8],
                job_role=role,
                search_queries=search_queries,
                max_videos_per_skill=2,
            )

        for resources in resources_list:
            with st.expander(f"📖 {resources.skill}"):
                col_v, col_c = st.columns(2)
                with col_v:
                    st.markdown("**📺 YouTube**")
                    for v in resources.videos:
                        if v.thumbnail:
                            st.image(v.thumbnail, width=180)
                        st.markdown(f"[{v.title}]({v.url})")
                        if v.channel and v.channel != "YouTube":
                            st.caption(f"Channel: {v.channel}")
                with col_c:
                    st.markdown("**🎓 Online Courses**")
                    for course in resources.courses:
                        st.markdown(f"{course.icon} [{course.title}]({course.url})")

        # Export
        st.divider()
        st.subheader("📤 Export")
        import json as _json
        export = {
            "role": role,
            "skills_to_learn": skills,
            "learning_path": path,
        }
        st.download_button(
            "⬇️ Download Learning Path (JSON)",
            data=_json.dumps(export, indent=2),
            file_name=f"learning_path_{role.replace(' ', '_').lower()}.json",
            mime="application/json",
        )
