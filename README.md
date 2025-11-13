# PPT-Agent Checker
## 📌 Overview  
PPT-Agent Checker is an AI-powered tool that analyzes PowerPoint presentations for:
- **Grammar and spelling issues** (Greek & English)
- **Logical flow and clarity**
- **Consistency of topics**
- **Actionable improvement suggestions**  

It uses **Azure OpenAI** for language analysis and embeddings, combined with `python-pptx` for slide parsing.

## 🏗 Architecture
```
PPT-Agent-Checker/
│
├── Output/
│   ├── ppt_report.html       # Results in HTML Format
│   ├── ppt_report.json       # Results in JSON Format
|
├── ppt_checker/
│   ├── loader.py              # Extracts text from slides
│   ├── grammar_checks.py      # Grammar & spelling analysis (Greek & English)
│   ├── flow_checks.py         # Logical flow and clarity analysis
│   ├── consistency_checks.py  # Topic consistency using embeddings
│   ├── fix_suggestions.py     # Generates improvement suggestions
│   ├── report_generator.py    # Creates HTML & JSON reports
|   ├── utils.py               # Helper for JSON extraction
|   ├── ppt_agent.py           # Main orchestrator
|
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (Azure OpenAI credentials)
├── README.md              # Project documentation
└── testing.py             # Example script to run the agent
```

## ⚙️ How It Works
1. **Load PPT** → Extract text from all slides.
2. **Run Checks**:
   - Grammar & spelling (LLM)
   - Flow & clarity (LLM)
   - Consistency (LLM + embeddings)
3. **Generate Reports**:
   - JSON (structured data)
   - HTML (user-friendly view)
4. **Suggest Fixes** → Actionable recommendations in the language of the presentation.

## ✅ Setup Instructions

### 1. Clone the Repository
```bash
    git clone https://github.com/your-repo/ppt-agent-checker.git
    cd ppt-agent-checker/ppt_checker
```
### 2. Create Virtual Environment
- For Linux/Mac
```
    python3 -m venv .venv
    source .venv/bin/activate
```
- For Windows
```
    python -m venv .venv
    .venv\Scripts\activate
```
### 3. Install Dependencies
```
    pip install -r requirements.txt
```
## ✅ Environment Variables (.env)
Create a .env file in the root folder with :
```
    OPENAI_API_KEY=your-azure-openai-key
    AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
    AZURE_OPENAI_API_VERSION=2024-06-01
    AZURE_OPENAI_DEPLOYMENT=your-chatgpt-deployment-name
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT=your-embedding-deployment-name
```

## 🔑 Configuration Notes

- **AZURE_OPENAI_DEPLOYMENT** → The name of your **ChatGPT model deployment** in Azure OpenAI (e.g., `gpt-4`, `gpt-4o`, or `gpt-5`).
- **AZURE_OPENAI_EMBEDDING_DEPLOYMENT** → The name of your **Embedding model deployment** in Azure OpenAI (e.g., `text-embedding-ada-002`).

> ⚠️ These names must match the **deployment names** you created in Azure OpenAI Studio, not just the model names.

## ✅ Run the Agent
Edit testing.py adding your powerpoint file path. The move inside ppt_checker folder with:
```
    cd ppt_agent/
```
and run the script using:
- For Linuc/Mac
```
    python3 ppt_agent.py
```
- For Windows
```
    python ppt_agent.py
```

## Output
- ppt_report.json → Full structured report
- ppt_report.html → User-friendly HTML report with tables and color coding

## Features
- Detects language and returns suggestions in Greek or English automatically.
- HTML report with tables, colors, and sections.
- Modular design for easy extension.
- Ready for auto-fix feature (coming soon).