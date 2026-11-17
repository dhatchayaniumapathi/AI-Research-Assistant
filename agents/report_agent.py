
from datetime import datetime


def clean_excerpt(content, max_length=500):
    content = " ".join(content.split())

    if len(content) <= max_length:
        return content

    excerpt = content[:max_length]

    # Find the last complete sentence within the limit
    sentence_end = max(
        excerpt.rfind(". "),
        excerpt.rfind("? "),
        excerpt.rfind("! ")
    )

    if sentence_end > 200:
        return excerpt[:sentence_end + 1]

    # If no suitable sentence boundary exists, end at a word
    return excerpt.rsplit(" ", 1)[0] + "..."


def generate_report(summary_data):

    topic = summary_data["topic"]
    summary = summary_data["summary"]
    sources = summary_data["sources"]

    report = f"""
# AI RESEARCH REPORT

## Research Topic
{topic}

## Generated On
{datetime.now().strftime("%d-%m-%Y %H:%M")}

---

## Executive Summary

{summary}

---

## Research Sources

"""

    for index, source in enumerate(sources, 1):
        excerpt = clean_excerpt(source.get("content", ""))

        report += f"""
### Source {index}: {source['title']}

- **URL:** {source['url']}
- **Information:** {excerpt}

"""

    report += """
---

*Generated using Multi-Agent AI Research Assistant*
"""

    return report
