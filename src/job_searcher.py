"""Job search abstraction — fetches job postings from JSearch API (RapidAPI).

JSearch aggregates listings from LinkedIn, Indeed, Glassdoor and other boards
legally via their public-facing job search pages.

Falls back to curated mock data when no API key is available so the app
remains demoable without any API credentials.
"""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any, Optional

import requests

JSEARCH_BASE = "https://jsearch.p.rapidapi.com/search"

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class JobPosting:
    id: str
    title: str
    company: str
    location: str
    description: str
    url: str
    source: str  # e.g. "LinkedIn", "Indeed", "Glassdoor"
    date_posted: str = ""
    employment_type: str = ""
    is_remote: bool = False
    skills_raw: list[str] = field(default_factory=list)

    def fingerprint(self) -> str:
        """Stable hash for deduplication across boards."""
        key = f"{self.title}|{self.company}|{self.location}"
        return hashlib.md5(key.lower().encode()).hexdigest()


# ---------------------------------------------------------------------------
# In-process TTL cache (avoids redundant API calls within a session)
# ---------------------------------------------------------------------------

_cache: dict[str, tuple[float, list[JobPosting]]] = {}


def _cache_get(key: str, ttl: int) -> Optional[list[JobPosting]]:
    if key in _cache:
        ts, data = _cache[key]
        if time.time() - ts < ttl:
            return data
    return None


def _cache_set(key: str, data: list[JobPosting]) -> None:
    _cache[key] = (time.time(), data)


# ---------------------------------------------------------------------------
# JSearch provider
# ---------------------------------------------------------------------------


def _jsearch_fetch(
    query: str,
    api_key: str,
    max_results: int = 20,
    location: str = "",
    remote_only: bool = False,
) -> list[JobPosting]:
    params: dict[str, Any] = {
        "query": query if not location else f"{query} in {location}",
        "page": "1",
        "num_pages": "1",
        "date_posted": "all",
    }
    if remote_only:
        params["remote_jobs_only"] = "true"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com",
    }

    resp = requests.get(JSEARCH_BASE, headers=headers, params=params, timeout=15)
    resp.raise_for_status()
    raw = resp.json().get("data", [])

    postings: list[JobPosting] = []
    seen: set[str] = set()

    for item in raw[:max_results]:
        posting = JobPosting(
            id=item.get("job_id", ""),
            title=item.get("job_title", ""),
            company=item.get("employer_name", ""),
            location=f"{item.get('job_city', '')}, {item.get('job_country', '')}".strip(", "),
            description=item.get("job_description", ""),
            url=item.get("job_apply_link", item.get("job_google_link", "")),
            source=item.get("job_publisher", ""),
            date_posted=item.get("job_posted_at_datetime_utc", ""),
            employment_type=item.get("job_employment_type", ""),
            is_remote=item.get("job_is_remote", False),
            skills_raw=item.get("job_required_skills") or [],
        )
        fp = posting.fingerprint()
        if fp not in seen:
            seen.add(fp)
            postings.append(posting)

    return postings


# ---------------------------------------------------------------------------
# Mock data — used when no API key is provided
# ---------------------------------------------------------------------------

_MOCK_JOBS: list[dict[str, Any]] = [
    {
        "id": "mock-1",
        "title": "Senior Data Scientist",
        "company": "Acme Analytics",
        "location": "San Francisco, US",
        "description": (
            "We are looking for a Senior Data Scientist to join our ML platform team. "
            "Requirements: Python, PyTorch or TensorFlow, SQL, Statistics, A/B testing, "
            "MLflow, Docker, experience with large-scale datasets, communication skills."
        ),
        "url": "https://example.com/job/1",
        "source": "Demo (mock data)",
        "employment_type": "FULLTIME",
        "is_remote": False,
        "skills_raw": ["Python", "PyTorch", "SQL", "Statistics", "Docker", "MLflow"],
    },
    {
        "id": "mock-2",
        "title": "Data Scientist",
        "company": "TechCorp",
        "location": "Remote",
        "description": (
            "Join our data team! Must have: Python, scikit-learn, pandas, "
            "machine learning, data visualization (Tableau or Power BI), "
            "SQL, cloud experience (AWS or GCP), collaborative mindset."
        ),
        "url": "https://example.com/job/2",
        "source": "Demo (mock data)",
        "employment_type": "FULLTIME",
        "is_remote": True,
        "skills_raw": ["Python", "scikit-learn", "pandas", "SQL", "AWS", "Tableau"],
    },
    {
        "id": "mock-3",
        "title": "Machine Learning Engineer",
        "company": "StartupXYZ",
        "location": "New York, US",
        "description": (
            "Build and deploy ML models at scale. Key skills: Python, TensorFlow, "
            "Kubernetes, CI/CD pipelines, REST APIs, model monitoring, Spark, "
            "distributed computing, software engineering best practices."
        ),
        "url": "https://example.com/job/3",
        "source": "Demo (mock data)",
        "employment_type": "FULLTIME",
        "is_remote": False,
        "skills_raw": ["Python", "TensorFlow", "Kubernetes", "Spark", "REST APIs"],
    },
    {
        "id": "mock-4",
        "title": "Data Scientist - NLP",
        "company": "AI Ventures",
        "location": "London, UK",
        "description": (
            "NLP-focused data scientist role. Required: Python, transformers / HuggingFace, "
            "BERT, GPT fine-tuning, spaCy, text classification, SQL, "
            "experience with LLMs, research mindset, publication record a plus."
        ),
        "url": "https://example.com/job/4",
        "source": "Demo (mock data)",
        "employment_type": "FULLTIME",
        "is_remote": True,
        "skills_raw": ["Python", "HuggingFace", "BERT", "spaCy", "SQL", "LLMs"],
    },
    {
        "id": "mock-5",
        "title": "Junior Data Scientist",
        "company": "DataFirst Inc.",
        "location": "Austin, US",
        "description": (
            "Entry-level DS position. Nice to have: Python, R, statistics, "
            "machine learning basics, SQL, Excel, data cleaning, Jupyter notebooks, "
            "strong academic background, internship experience preferred."
        ),
        "url": "https://example.com/job/5",
        "source": "Demo (mock data)",
        "employment_type": "FULLTIME",
        "is_remote": False,
        "skills_raw": ["Python", "R", "SQL", "Statistics", "Excel"],
    },
]


def _mock_fetch(query: str, max_results: int) -> list[JobPosting]:
    postings = [
        JobPosting(**{k: v for k, v in job.items()})
        for job in _MOCK_JOBS[:max_results]
    ]
    return postings


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


class JobSearcher:
    def __init__(self, api_key: Optional[str], cache_ttl: int = 3600) -> None:
        self.api_key = api_key
        self.cache_ttl = cache_ttl
        self.using_mock = not bool(api_key)

    def search(
        self,
        job_role: str,
        location: str = "",
        remote_only: bool = False,
        max_results: int = 20,
    ) -> tuple[list[JobPosting], bool]:
        """Return (postings, is_mock).  Cached per query string."""
        cache_key = f"{job_role}|{location}|{remote_only}|{max_results}"
        cached = _cache_get(cache_key, self.cache_ttl)
        if cached is not None:
            return cached, self.using_mock

        if self.using_mock:
            results = _mock_fetch(job_role, max_results)
        else:
            try:
                results = _jsearch_fetch(
                    query=job_role,
                    api_key=self.api_key,
                    max_results=max_results,
                    location=location,
                    remote_only=remote_only,
                )
            except requests.HTTPError as exc:
                raise RuntimeError(
                    f"JSearch API error {exc.response.status_code}: {exc.response.text[:200]}"
                ) from exc
            except requests.RequestException as exc:
                raise RuntimeError(f"Network error contacting JSearch: {exc}") from exc

        _cache_set(cache_key, results)
        return results, self.using_mock

    def top_companies(self, postings: list[JobPosting]) -> list[tuple[str, int]]:
        """Return companies sorted by job-posting count."""
        counts: dict[str, int] = {}
        for p in postings:
            counts[p.company] = counts.get(p.company, 0) + 1
        return sorted(counts.items(), key=lambda x: x[1], reverse=True)
