import openai
import os
import json
import langdetect
from utils import extract_json

def check_spelling_and_grammar(slides_text, chunk_size=3):
    """
    Checks spelling and grammar for Greek and English with chunking.
    Detects language per chunk and applies style guide rules.
    """
    issues = []
    for i in range(0, len(slides_text), chunk_size):
        chunk = slides_text[i:i+chunk_size]
        lang = "mixed"
        try:
            combined_text = " ".join([slide['title'] + " " + " ".join(slide['content']) for slide in chunk])
            lang = langdetect.detect(combined_text)
        except:
            pass

        style_note = "Ensure proper capitalization and punctuation."
        language_instruction = "Όλες οι προτάσεις να είναι στα ελληνικά." if lang == "el" else "All suggestions should be in English."

        prompt = f"""
        Analyze these slides for spelling and grammar issues in {lang}:
        {json.dumps(chunk, ensure_ascii=False)}

        Tasks:
        1. Identify spelling and grammar mistakes.
        2. Suggest corrections.
        3. Apply style guide: {style_note}.
        {language_instruction}
        Return JSON:
        {{
          "issues": [
            {{
              "slide_number": X,
              "errors": [
                {{"error": "...", "suggestion": "..."}}
              ]
            }}
          ]
        }}
        """

        response = openai.ChatCompletion.create(
            engine=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {"role": "system", "content": "You are an expert in Greek and English grammar."},
                {"role": "user", "content": prompt}
            ]
        )

        raw_content = response.choices[0].message["content"]
        parsed = extract_json(raw_content)
        issues.extend(parsed.get("issues", []))

    return issues