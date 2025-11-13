import os
import json
from datetime import datetime

# Get absolute path to the project root (parent of this file’s folder)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_DIR = os.path.join(ROOT_DIR, "Output")

def export_html_report(report, output_path=None):
    # If no custom path given, use default in root Output folder
    if output_path is None:
        output_path = os.path.join(OUTPUT_DIR, "ppt_report.html")

    # Make sure Output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>PPT Analysis Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background: #f9f9f9; }}
            h1 {{ color: #2c3e50; }}
            .section {{ background: #fff; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
            .error {{ color: #c0392b; font-weight: bold; }}
            .suggestion {{ color: #27ae60; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; }}
            th {{ background: #34495e; color: white; }}
            .badge {{ display: inline-block; padding: 5px 10px; border-radius: 5px; font-size: 12px; }}
            .badge-error {{ background: #e74c3c; color: white; }}
            .badge-ok {{ background: #2ecc71; color: white; }}
        </style>
    </head>
    <body>
        <h1>PPT Analysis Report</h1>
        <p><strong>Date:</strong> {datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
    """

    # Grammar Issues
    html += "<div class='section'><h2>Grammar Issues</h2>"
    if report.get("grammar_issues"):
        html += "<table><tr><th>Slide</th><th>Error</th><th>Suggestion</th></tr>"
        for issue in report["grammar_issues"]:
            slide = issue.get("slide_number", "-")
            for err in issue.get("errors", []):
                html += f"<tr><td>{slide}</td><td class='error'>{err['error']}</td><td class='suggestion'>{err['suggestion']}</td></tr>"
        html += "</table>"
    else:
        html += "<p class='badge badge-ok'>No grammar issues found.</p>"
    html += "</div>"

    # Flow Analysis
    html += "<div class='section'><h2>Flow Analysis</h2>"
    flow = report.get("flow_analysis", {})
    html += f"<p><strong>Summary:</strong> {flow.get('flow_analysis', 'N/A')}</p>"
    html += "<h3>Missing Sections:</h3><ul>"
    for item in flow.get("missing_sections", []):
        html += f"<li class='error'>{item}</li>"
    html += "</ul><h3>Redundant Sections:</h3><ul>"
    for item in flow.get("redundant_sections", []):
        html += f"<li>{item}</li>"
    html += "</ul><h3>Clarity Improvements:</h3><ul>"
    for item in flow.get("clarity_improvements", []):
        html += f"<li class='suggestion'>{item}</li>"
    html += "</ul></div>"

    # Consistency
    html += "<div class='section'><h2>Consistency Check</h2>"
    consistency = report.get("consistency_dynamic", {})
    html += "<h3>Main Topics:</h3><ul>"
    for topic in consistency.get("topics", []):
        html += f"<li>{topic}</li>"
    html += "</ul><h3>Issues:</h3>"
    if consistency.get("issues"):
        html += "<table><tr><th>Slide</th><th>Missing Topic</th><th>Similarity Score</th></tr>"
        for issue in consistency["issues"]:
            html += f"<tr><td>{issue['slide_number']}</td><td class='error'>{issue['missing_topic']}</td><td>{issue['similarity_score']}</td></tr>"
        html += "</table>"
    else:
        html += "<p class='badge badge-ok'>No consistency issues found.</p>"
    html += "</div></body></html>"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path


def export_json_report(report, output_path=None):
    if output_path is None:
        output_path = os.path.join(OUTPUT_DIR, "ppt_report.json")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    return output_path
