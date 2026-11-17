
from utils.web_search import search_web


def research_topic(topic):

    print(f"Researching: {topic}")

    # Step 1: Search the web using Tavily
    search_results = search_web(topic)

    if not search_results:
        raise ValueError("No research results found. Try another topic.")

    # Step 2: Collect information from search results
    context = ""

    for index, result in enumerate(search_results, 1):
        context += f"""
Source {index}
Title: {result['title']}
URL: {result['url']}
Content: {result['content']}
"""

    # Step 3: Return raw research findings
    return {
        "topic": topic,
        "findings": context,
        "sources": search_results
    }
