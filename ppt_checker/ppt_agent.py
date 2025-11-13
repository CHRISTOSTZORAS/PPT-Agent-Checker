import os
import json
from dotenv import load_dotenv
import openai

from loader import load_presentation
from grammar_checks import check_spelling_and_grammar
from flow_checks import analyze_flow_and_clarity
from consistency_checks import check_consistency_dynamic
from report_generator import export_html_report, export_json_report
from fix_suggestions import suggest_fixes

load_dotenv()
openai.api_type = "azure"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")

class PPTAgent:
    def __init__(self, file_path):
        self.file_path = file_path
        self.slides = load_presentation(file_path)
        self.report = {}

    def run_checks(self):
        print("Running grammar and spelling checks...")
        self.report["grammar_issues"] = check_spelling_and_grammar(self.slides)

        print("Analyzing flow and clarity...")
        self.report["flow_analysis"] = analyze_flow_and_clarity(self.slides)

        print("Checking dynamic consistency...")
        self.report["consistency_dynamic"] = check_consistency_dynamic(self.slides)

        return self.report

    def export_reports(self):
        print("Exporting reports...")
        json_path = export_json_report(self.report)
        html_path = export_html_report(self.report)
        return {"json": json_path, "html": html_path}

    def suggest_improvements(self):
        print("Generating improvement suggestions...")
        return suggest_fixes(self.report)

if __name__ == "__main__":
    agent = PPTAgent("/path/to/your/presentation.pptx")
    report = agent.run_checks()
    print(json.dumps(report, indent=4, ensure_ascii=False))

    paths = agent.export_reports()
    print(f"Reports saved: {paths}")

    fixes = agent.suggest_improvements()
    print(json.dumps(fixes, indent=4, ensure_ascii=False))