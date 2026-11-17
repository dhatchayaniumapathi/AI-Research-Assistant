
from tavily import TavilyClient
from config import TAVILY_API_KEY

tavily = TavilyClient(api_key=TAVILY_API_KEY)

TRUSTED_DOMAINS = [
    "edu",
    "gov",
    "org",
    "nature.com",
    "sciencedirect.com",
    "brookings.edu",
    "unesco.org",
    "oecd.org",
    "who.int"
]


def search_web(query):

    response = tavily.search(
        query=query,
        search_depth="basic",
        max_results=8
    )

    results = []
    seen_urls = set()

    for item in response.get("results", []):

        title = item.get("title")
        url = item.get("url")
        content = item.get("content")

        if not title or not url or not content:
            continue

        if url in seen_urls:
            continue

        seen_urls.add(url)

        domain = url.lower().split("/")[2]

        is_trusted = (
            domain.endswith(".edu")
            or domain.endswith(".gov")
            or domain.endswith(".org")
            or any(site in domain for site in TRUSTED_DOMAINS)
        )

        results.append({
            "title": title,
            "url": url,
            "content": content,
            "trusted": is_trusted
        })

    results.sort(
        key=lambda item: item["trusted"],
        reverse=True
    )

    return results[:3]
