import openai
import os
import json
from utils import extract_json

def analyze_flow_and_clarity(slides_text):
    prompt = f"""
    Είσαι ειδικός στην αξιολόγηση παρουσιάσεων.
    Ανάλυσε τις παρακάτω διαφάνειες για:
    1. Λογική ροή (ακολουθεί ξεκάθαρη δομή;).
    2. Ελλείποντα ή περιττά τμήματα.
    3. Ασαφείς ή παραπλανητικές δηλώσεις.
    4. Προτάσεις για βελτίωση.

    Όλες οι προτάσεις να είναι στη γλώσσα της παρουσίασης (αν είναι ελληνικά, απάντησε στα ελληνικά).

    Διαφάνειες:
    {json.dumps(slides_text, ensure_ascii=False)}

    Επιστροφή σε JSON:
    {{
      "flow_analysis": "...",
      "missing_sections": [...],
      "redundant_sections": [...],
      "misleading_statements": [...],
      "clarity_improvements": [...]
    }}
    """

    response = openai.ChatCompletion.create(
        engine=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": "Είσαι ειδικός στην ανάλυση παρουσιάσεων."},
            {"role": "user", "content": prompt}
        ]
    )

    raw_content = response.choices[0].message["content"]
    return extract_json(raw_content)