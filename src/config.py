"""Configuration management: supports both .env files and runtime UI-provided keys."""
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")


@dataclass
class Config:
    openai_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("OPENAI_API_KEY")
    )
    jsearch_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("JSEARCH_API_KEY")
    )
    youtube_api_key: Optional[str] = field(
        default_factory=lambda: os.getenv("YOUTUBE_API_KEY")
    )
    openai_model: str = field(
        default_factory=lambda: os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    )
    max_jobs_per_search: int = field(
        default_factory=lambda: int(os.getenv("MAX_JOBS_PER_SEARCH", "20"))
    )
    cache_ttl_seconds: int = field(
        default_factory=lambda: int(os.getenv("CACHE_TTL_SECONDS", "3600"))
    )

    def update_from_ui(
        self,
        openai_key: Optional[str] = None,
        jsearch_key: Optional[str] = None,
        youtube_key: Optional[str] = None,
    ) -> None:
        """Allow runtime override from Streamlit sidebar inputs."""
        if openai_key:
            self.openai_api_key = openai_key
        if jsearch_key:
            self.jsearch_api_key = jsearch_key
        if youtube_key:
            self.youtube_api_key = youtube_key

    @property
    def has_openai(self) -> bool:
        return bool(self.openai_api_key)

    @property
    def has_jsearch(self) -> bool:
        return bool(self.jsearch_api_key)

    @property
    def has_youtube(self) -> bool:
        return bool(self.youtube_api_key)
