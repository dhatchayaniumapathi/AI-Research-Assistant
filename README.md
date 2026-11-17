# AI Research Assistant

### Multi-Agent Generative AI Research System

An AI-powered research assistant that automates web research, information summarization, and report generation using a multi-agent workflow.

## Features

- **Automated Web Research:** Retrieves relevant information from the web using Tavily.
- **AI-Powered Summarization:** Uses Google Gemini to analyze research findings and generate structured summaries.
- **Automated Report Generation:** Generates professional Markdown research reports.
- **Source References:** Includes source titles, URLs, and information excerpts.
- **Downloadable Reports:** Allows users to download generated research reports.
- **Interactive Interface:** Provides a simple user interface using Gradio.

## Multi-Agent Architecture

The system consists of three specialized agents:

| Agent | Responsibility | Technology |
|---|---|---|
| Research Agent | Searches the web and collects relevant information | Tavily API |
| Summarization Agent | Analyzes findings and creates structured summaries | Google Gemini |
| Report Agent | Generates formatted research reports | Python |

### Workflow

1. User enters a research topic.
2. Research Agent retrieves relevant web information.
3. Summarization Agent analyzes and summarizes the findings.
4. Report Agent generates a structured research report.
5. User views and downloads the report.

## Technology Stack

- Python
- Google Gemini API
- Tavily Search API
- Gradio
- Requests
- Python-dotenv

## Project Structure

```text
AI-Research-Assistant/
│
├── agents/
│   ├── __init__.py
│   ├── research_agent.py
│   ├── summarizer_agent.py
│   └── report_agent.py
│
├── utils/
│   ├── __init__.py
│   └── web_search.py
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Research-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Obtain API keys from:

- [Google AI Studio](https://aistudio.google.com/)
- [Tavily](https://tavily.com/)

### 5. Run the Application

```bash
python app.py
```

Open the local Gradio URL displayed in the terminal.

## Sample Research Topics

- Benefits and risks of AI tutoring in schools
- Impact of artificial intelligence on healthcare
- How generative AI is changing software development

## Security

API keys are stored in environment variables and should never be committed to the public repository.

## Project Objective

To demonstrate how multiple specialized AI agents can collaborate to automate research, summarize web information, and generate structured reports.

---

**Developed as an AI internship mini-project.**