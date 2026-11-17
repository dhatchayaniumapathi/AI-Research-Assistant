
from config import generate_with_retry


def summarize_research(research_data):

    topic = research_data["topic"]
    findings = research_data["findings"]

    prompt = f"""
    You are an expert research summarization assistant.

    Research Topic: {topic}

    Research Findings:
    {findings}

    Create a concise but informative summary containing:

    1. Overview
    2. Five Key Takeaways
    3. Major Trends
    4. Important Insights
    5. Conclusion

    Use clear professional language.
    Do not introduce information that is not present
    in the research findings.
    Include source references where relevant.
    """

    response_text = generate_with_retry(prompt)

    return {
        "topic": topic,
        "summary": response_text,
        "sources": research_data["sources"]
    }
