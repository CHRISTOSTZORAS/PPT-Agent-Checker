import openai
import os
import json
from utils import extract_json

def suggest_fixes(report):
    prompt = f"""
    Με βάση αυτό το report, πρότεινε διορθώσεις στα εξής:
    - Γραμματική και ορθογραφία
    - Λογική ροή
    - Συνέπεια

    Όλες οι προτάσεις να είναι στη γλώσσα της παρουσίασης (αν είναι ελληνικά, απάντησε στα ελληνικά).

    Report:
    {json.dumps(report, ensure_ascii=False)}

    Επιστροφή σε JSON:
    {{
    "grammar_fixes": [...],
    "flow_fixes": [...],
    "consistency_fixes": [...]
    }}
    """
    response = openai.ChatCompletion.create(
        engine=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": "Είσαι ειδικός στη βελτίωση παρουσιάσεων."},
            {"role": "user", "content": prompt}
        ]
    )

    raw_content = response.choices[0].message["content"]
    return extract_json(raw_content)