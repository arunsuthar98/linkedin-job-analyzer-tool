"""Skill analyzer — normalises raw skills against a taxonomy and deduplicates synonyms."""
from __future__ import annotations

# Synonym map: canonical name → list of aliases (all lowercase)
_SYNONYMS: dict[str, list[str]] = {
    "Python": ["python3", "python 3", "py"],
    "JavaScript": ["js", "javascript", "ecmascript"],
    "TypeScript": ["ts", "typescript"],
    "TensorFlow": ["tensorflow", "tf"],
    "PyTorch": ["pytorch", "torch"],
    "scikit-learn": ["sklearn", "scikit learn", "scikit-learn"],
    "HuggingFace": ["huggingface", "hugging face", "transformers"],
    "Machine Learning": ["ml", "machine learning"],
    "Deep Learning": ["dl", "deep learning"],
    "Natural Language Processing": ["nlp", "natural language processing"],
    "Computer Vision": ["cv", "computer vision"],
    "SQL": ["sql", "structured query language"],
    "PostgreSQL": ["postgres", "postgresql"],
    "MySQL": ["mysql"],
    "MongoDB": ["mongodb", "mongo"],
    "AWS": ["amazon web services", "aws"],
    "GCP": ["google cloud", "gcp", "google cloud platform"],
    "Azure": ["microsoft azure", "azure"],
    "Docker": ["docker"],
    "Kubernetes": ["kubernetes", "k8s"],
    "Git": ["git", "github", "gitlab", "version control"],
    "REST APIs": ["rest api", "rest apis", "restful", "api development"],
    "FastAPI": ["fastapi"],
    "Flask": ["flask"],
    "Django": ["django"],
    "React": ["reactjs", "react.js"],
    "Spark": ["apache spark", "pyspark", "spark"],
    "Tableau": ["tableau"],
    "Power BI": ["power bi", "powerbi"],
    "Excel": ["microsoft excel", "excel"],
    "R": [" r ", "r programming", "rlang"],
    "Statistics": ["statistical analysis", "statistics", "statistical modelling"],
    "MLflow": ["mlflow"],
    "Airflow": ["apache airflow", "airflow"],
    "CI/CD": ["ci/cd", "cicd", "continuous integration", "continuous deployment"],
}

# Build reverse lookup: alias → canonical
_ALIAS_TO_CANONICAL: dict[str, str] = {}
for canonical, aliases in _SYNONYMS.items():
    _ALIAS_TO_CANONICAL[canonical.lower()] = canonical
    for alias in aliases:
        _ALIAS_TO_CANONICAL[alias.strip()] = canonical


def normalize_skill(raw: str) -> str:
    """Return the canonical form of a skill, or the original if unknown."""
    return _ALIAS_TO_CANONICAL.get(raw.strip().lower(), raw.strip())


def normalize_skills(skills: list[str]) -> list[str]:
    """Normalise and deduplicate a list of skills."""
    seen: set[str] = set()
    result: list[str] = []
    for s in skills:
        canonical = normalize_skill(s)
        if canonical not in seen:
            seen.add(canonical)
            result.append(canonical)
    return result


def frequency_map(skills_lists: list[list[str]]) -> dict[str, int]:
    """Count how many postings mention each normalised skill."""
    counts: dict[str, int] = {}
    for skills in skills_lists:
        for skill in normalize_skills(skills):
            counts[skill] = counts.get(skill, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
