# testing.py
from ppt_agent import PPTAgent
import json

# Path to your PPT file
ppt_path = r"your_path.pptx"

# Initialize agent
agent = PPTAgent(ppt_path)

# Run all checks
print("Running checks...")
report = agent.run_checks()

# Print report in console
print(json.dumps(report, indent=4, ensure_ascii=False))

# Export reports
paths = agent.export_reports()
print(f"Reports saved at: {paths}")

# Suggest improvements
fixes = agent.suggest_improvements()
print("Suggested fixes:")
print(json.dumps(fixes, indent=4, ensure_ascii=False))