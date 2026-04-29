"""Learning recommender — fetches real YouTube videos and generates
deep-link search URLs for Coursera, Udemy, and edX.

YouTube results are fetched via the Data API v3 when a key is available.
Falls back to pre-built search URLs so users can always find resources.
"""
from __future__ import annotations

import urllib.parse
from dataclasses import dataclass, field
from typing import Optional

import requests


@dataclass
class VideoResource:
    title: str
    channel: str
    url: str
    thumbnail: str = ""
    duration: str = ""


@dataclass
class CourseLink:
    platform: str
    title: str
    url: str
    icon: str = ""


@dataclass
class LearningResources:
    skill: str
    videos: list[VideoResource] = field(default_factory=list)
    courses: list[CourseLink] = field(default_factory=list)


YOUTUBE_SEARCH_API = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_DETAILS_API = "https://www.googleapis.com/youtube/v3/videos"


def _yt_search(query: str, api_key: str, max_results: int = 3) -> list[VideoResource]:
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "order": "relevance",
        "key": api_key,
    }
    resp = requests.get(YOUTUBE_SEARCH_API, params=params, timeout=10)
    resp.raise_for_status()
    items = resp.json().get("items", [])

    videos: list[VideoResource] = []
    for item in items:
        vid_id = item["id"]["videoId"]
        snippet = item["snippet"]
        videos.append(
            VideoResource(
                title=snippet.get("title", ""),
                channel=snippet.get("channelTitle", ""),
                url=f"https://www.youtube.com/watch?v={vid_id}",
                thumbnail=snippet.get("thumbnails", {})
                .get("medium", {})
                .get("url", ""),
            )
        )
    return videos


def _course_links(skill: str, job_role: str) -> list[CourseLink]:
    query = urllib.parse.quote_plus(f"{skill} {job_role}")
    return [
        CourseLink(
            platform="Coursera",
            title=f'Search "{skill}" on Coursera',
            url=f"https://www.coursera.org/search?query={query}",
            icon="🎓",
        ),
        CourseLink(
            platform="Udemy",
            title=f'Search "{skill}" on Udemy',
            url=f"https://www.udemy.com/courses/search/?q={query}",
            icon="📘",
        ),
        CourseLink(
            platform="edX",
            title=f'Search "{skill}" on edX',
            url=f"https://www.edx.org/search?q={query}",
            icon="🏛️",
        ),
        CourseLink(
            platform="freeCodeCamp",
            title=f'Search "{skill}" on freeCodeCamp',
            url=f"https://www.freecodecamp.org/news/search/?query={urllib.parse.quote_plus(skill)}",
            icon="🔥",
        ),
    ]


class LearningRecommender:
    def __init__(self, youtube_api_key: Optional[str] = None) -> None:
        self.yt_key = youtube_api_key

    def get_resources(
        self,
        skill: str,
        job_role: str,
        yt_query_override: Optional[str] = None,
        max_videos: int = 3,
    ) -> LearningResources:
        """Return videos + course links for a single skill."""
        yt_query = yt_query_override or f"{skill} tutorial for {job_role}"
        videos: list[VideoResource] = []

        if self.yt_key:
            try:
                videos = _yt_search(yt_query, self.yt_key, max_results=max_videos)
            except requests.RequestException:
                # Gracefully fall through to URL-only mode
                pass

        if not videos:
            # Provide a YouTube search URL as a fallback
            videos = [
                VideoResource(
                    title=f'Search YouTube: "{yt_query}"',
                    channel="YouTube",
                    url=f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(yt_query)}",
                )
            ]

        return LearningResources(
            skill=skill,
            videos=videos,
            courses=_course_links(skill, job_role),
        )

    def get_resources_for_skills(
        self,
        skills: list[str],
        job_role: str,
        search_queries: Optional[dict[str, dict[str, str]]] = None,
        max_videos_per_skill: int = 2,
    ) -> list[LearningResources]:
        """Return resources for each skill in the list."""
        results: list[LearningResources] = []
        for skill in skills[:10]:  # cap at 10 to avoid rate limits
            yt_query = None
            if search_queries and skill in search_queries:
                yt_query = search_queries[skill].get("youtube")
            results.append(
                self.get_resources(
                    skill=skill,
                    job_role=job_role,
                    yt_query_override=yt_query,
                    max_videos=max_videos_per_skill,
                )
            )
        return results
