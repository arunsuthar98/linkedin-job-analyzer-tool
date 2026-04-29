"""Certification recommender — maps job roles to relevant industry certifications.

Adapted from the BFSI Job Intelligence Agent pattern but generalized to
software engineering, data, cloud, security, AI/ML, product, finance and BFSI roles.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Certification:
    name: str
    provider: str
    url: str
    level: str = "Intermediate"  # Beginner / Intermediate / Advanced
    category: str = ""


CERT_CATALOG: dict[str, list[Certification]] = {
    # ── Cloud ────────────────────────────────────────────────────────────
    "aws": [
        Certification("AWS Certified Cloud Practitioner", "AWS",
                      "https://aws.amazon.com/certification/certified-cloud-practitioner/", "Beginner", "Cloud"),
        Certification("AWS Solutions Architect Associate", "AWS",
                      "https://aws.amazon.com/certification/certified-solutions-architect-associate/", "Intermediate", "Cloud"),
        Certification("AWS Solutions Architect Professional", "AWS",
                      "https://aws.amazon.com/certification/certified-solutions-architect-professional/", "Advanced", "Cloud"),
    ],
    "azure": [
        Certification("Microsoft Azure Fundamentals (AZ-900)", "Microsoft",
                      "https://learn.microsoft.com/certifications/azure-fundamentals/", "Beginner", "Cloud"),
        Certification("Azure Administrator Associate (AZ-104)", "Microsoft",
                      "https://learn.microsoft.com/certifications/azure-administrator/", "Intermediate", "Cloud"),
    ],
    "gcp": [
        Certification("Google Cloud Digital Leader", "Google",
                      "https://cloud.google.com/learn/certification/cloud-digital-leader", "Beginner", "Cloud"),
        Certification("Google Cloud Associate Cloud Engineer", "Google",
                      "https://cloud.google.com/learn/certification/cloud-engineer", "Intermediate", "Cloud"),
    ],

    # ── Data / Analytics ──────────────────────────────────────────────────
    "data": [
        Certification("Google Data Analytics Professional", "Google/Coursera",
                      "https://www.coursera.org/professional-certificates/google-data-analytics", "Beginner", "Data"),
        Certification("Microsoft Power BI Data Analyst (PL-300)", "Microsoft",
                      "https://learn.microsoft.com/certifications/power-bi-data-analyst-associate/", "Intermediate", "Data"),
        Certification("Tableau Desktop Specialist", "Tableau",
                      "https://www.tableau.com/learn/certification/desktop-specialist", "Beginner", "Data"),
        Certification("Databricks Lakehouse Fundamentals", "Databricks",
                      "https://www.databricks.com/learn/certification/lakehouse-fundamentals", "Beginner", "Data"),
    ],

    # ── AI / ML ───────────────────────────────────────────────────────────
    "ai": [
        Certification("DeepLearning.AI Machine Learning Specialization", "Coursera",
                      "https://www.coursera.org/specializations/machine-learning-introduction", "Intermediate", "AI/ML"),
        Certification("AWS Machine Learning Specialty", "AWS",
                      "https://aws.amazon.com/certification/certified-machine-learning-specialty/", "Advanced", "AI/ML"),
        Certification("TensorFlow Developer Certificate", "Google",
                      "https://www.tensorflow.org/certificate", "Intermediate", "AI/ML"),
        Certification("HuggingFace NLP Course (Free)", "HuggingFace",
                      "https://huggingface.co/learn/nlp-course", "Intermediate", "AI/ML"),
    ],

    # ── DevOps / SRE ──────────────────────────────────────────────────────
    "devops": [
        Certification("Certified Kubernetes Administrator (CKA)", "CNCF/Linux Foundation",
                      "https://www.cncf.io/training/certification/cka/", "Advanced", "DevOps"),
        Certification("Docker Certified Associate", "Docker",
                      "https://docker.com/certification", "Intermediate", "DevOps"),
        Certification("HashiCorp Certified: Terraform Associate", "HashiCorp",
                      "https://www.hashicorp.com/certification/terraform-associate", "Intermediate", "DevOps"),
    ],

    # ── Security ──────────────────────────────────────────────────────────
    "security": [
        Certification("CompTIA Security+", "CompTIA",
                      "https://www.comptia.org/certifications/security", "Beginner", "Security"),
        Certification("Certified Ethical Hacker (CEH)", "EC-Council",
                      "https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/", "Intermediate", "Security"),
        Certification("CISSP", "ISC2",
                      "https://www.isc2.org/Certifications/CISSP", "Advanced", "Security"),
        Certification("CISA", "ISACA",
                      "https://www.isaca.org/credentialing/cisa", "Advanced", "Security"),
    ],

    # ── Project / Product ─────────────────────────────────────────────────
    "pm": [
        Certification("Google Project Management Professional", "Coursera",
                      "https://www.coursera.org/professional-certificates/google-project-management", "Beginner", "Management"),
        Certification("PMP — Project Management Professional", "PMI",
                      "https://www.pmi.org/certifications/project-management-pmp", "Advanced", "Management"),
        Certification("Certified ScrumMaster (CSM)", "Scrum Alliance",
                      "https://www.scrumalliance.org/get-certified/practitioners/csm-certification", "Intermediate", "Management"),
        Certification("Professional Scrum Product Owner (PSPO)", "Scrum.org",
                      "https://www.scrum.org/professional-scrum-product-owner-certifications", "Intermediate", "Management"),
    ],

    # ── Finance / BFSI ────────────────────────────────────────────────────
    "finance": [
        Certification("CFA — Chartered Financial Analyst", "CFA Institute",
                      "https://www.cfainstitute.org/programs/cfa", "Advanced", "Finance"),
        Certification("FRM — Financial Risk Manager", "GARP",
                      "https://www.garp.org/frm", "Advanced", "Finance"),
        Certification("CIA — Certified Internal Auditor", "IIA",
                      "https://www.theiia.org/certifications/cia/", "Advanced", "Finance"),
        Certification("CAMS — Anti-Money Laundering", "ACAMS",
                      "https://www.acams.org/en/certifications/cams", "Intermediate", "Finance"),
    ],

    # ── Software / General ────────────────────────────────────────────────
    "software": [
        Certification("Meta Front-End Developer Professional", "Coursera",
                      "https://www.coursera.org/professional-certificates/meta-front-end-developer", "Beginner", "Software"),
        Certification("Meta Back-End Developer Professional", "Coursera",
                      "https://www.coursera.org/professional-certificates/meta-back-end-developer", "Intermediate", "Software"),
        Certification("Oracle Certified Professional: Java SE", "Oracle",
                      "https://education.oracle.com/java-se-certification", "Intermediate", "Software"),
    ],
}


# Maps job-role keywords to which certification categories apply
_KEYWORDS_TO_CATEGORIES: dict[str, list[str]] = {
    # Data
    "data scientist": ["data", "ai", "aws"],
    "data analyst": ["data"],
    "data engineer": ["data", "aws", "devops"],
    "machine learning": ["ai", "data"],
    "ml engineer": ["ai", "devops"],
    "ai engineer": ["ai"],
    "nlp": ["ai"],
    # Cloud / DevOps
    "cloud": ["aws", "azure", "gcp"],
    "devops": ["devops", "aws"],
    "sre": ["devops", "aws"],
    "site reliability": ["devops"],
    "platform engineer": ["devops", "aws"],
    "kubernetes": ["devops"],
    # Security
    "security": ["security"],
    "cybersecurity": ["security"],
    "penetration": ["security"],
    "soc analyst": ["security"],
    # Software
    "frontend": ["software"],
    "backend": ["software"],
    "full stack": ["software"],
    "software engineer": ["software", "aws"],
    "developer": ["software"],
    "java": ["software"],
    "python": ["software", "data"],
    # Product / PM
    "product manager": ["pm"],
    "project manager": ["pm"],
    "scrum master": ["pm"],
    "program manager": ["pm"],
    # Finance / BFSI
    "audit": ["finance"],
    "risk": ["finance"],
    "compliance": ["finance"],
    "investment": ["finance"],
    "financial analyst": ["finance"],
    "aml": ["finance"],
    "kyc": ["finance"],
}


def recommend_for_role(job_role: str, max_results: int = 6) -> list[Certification]:
    """Return top relevant certifications for a job role."""
    role_lower = job_role.lower()
    selected_categories: list[str] = []

    for keyword, cats in _KEYWORDS_TO_CATEGORIES.items():
        if keyword in role_lower:
            for c in cats:
                if c not in selected_categories:
                    selected_categories.append(c)

    if not selected_categories:
        selected_categories = ["software"]

    results: list[Certification] = []
    for cat in selected_categories:
        results.extend(CERT_CATALOG.get(cat, []))

    # Dedupe by name and limit
    seen: set[str] = set()
    unique: list[Certification] = []
    for cert in results:
        if cert.name not in seen:
            seen.add(cert.name)
            unique.append(cert)
        if len(unique) >= max_results:
            break
    return unique


def all_categories() -> list[str]:
    return sorted(CERT_CATALOG.keys())
