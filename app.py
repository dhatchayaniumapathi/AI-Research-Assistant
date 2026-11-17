import time
import gradio as gr
import tempfile
import os

from agents.research_agent import research_topic
from agents.summarizer_agent import summarize_research
from agents.report_agent import generate_report



def run_research(topic):

    if not topic.strip():
        raise gr.Error("Please enter a research topic.")

    try:
        start = time.perf_counter()

        print("\n========== RESEARCH STARTED ==========")

        # Agent 1
        stage = time.perf_counter()
        research_data = research_topic(topic)
        print(f"Research Agent: {time.perf_counter() - stage:.2f}s")

        if not isinstance(research_data, dict):
            raise ValueError("Research agent returned no valid findings.")

        # Agent 2
        stage = time.perf_counter()
        summary_data = summarize_research(research_data)
        print(f"Summarization Agent: {time.perf_counter() - stage:.2f}s")

        # Agent 3
        stage = time.perf_counter()
        report = generate_report(summary_data)
        print(f"Report Agent: {time.perf_counter() - stage:.2f}s")

        # Save report
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".md",
            delete=False,
            encoding="utf-8"
        ) as file:
            file.write(report)
            report_path = file.name

        print(f"TOTAL TIME: {time.perf_counter() - start:.2f}s")
        print("========== RESEARCH COMPLETED ==========\n")

        return report, report_path

    except Exception as error:
        print(f"ERROR: {error}")
        raise gr.Error(f"Research failed: {str(error)}")


# Gradio Interface
with gr.Blocks(title="AI Research Assistant") as demo:

    gr.Markdown("""
    # AI Research Assistant

    ### Multi-Agent Generative AI Research System

    Enter a topic and let three AI agents
    research, summarize and generate a report.
    """)

    topic_input = gr.Textbox(
        label="Research Topic",
        placeholder="Example: Impact of Artificial Intelligence in Healthcare",
        lines=2
    )

    research_button = gr.Button(
        "Start AI Research",
        variant="primary"
    )

    report_output = gr.Markdown(
        label="Generated Research Report"
    )

    download_output = gr.File(
        label="Download Research Report"
    )

    research_button.click(
        fn=run_research,
        inputs=topic_input,
        outputs=[report_output, download_output]
    )

demo.launch()
