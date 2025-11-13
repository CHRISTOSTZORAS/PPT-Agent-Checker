import re
import json

def extract_json(text):
    """
    Extract JSON object from model response safely.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in response")
    else:
        raise ValueError("No JSON found in response")