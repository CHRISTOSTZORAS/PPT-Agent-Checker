import openai
import os
import json
from sklearn.metrics.pairwise import cosine_similarity
from utils import extract_json

def extract_main_topics(slides_text, top_n=5):
    prompt = f"""
    Ανάλυσε τις παρακάτω διαφάνειες και εξήγαγε τα {top_n} πιο σημαντικά θέματα ή λέξεις-κλειδιά:
    {json.dumps(slides_text, ensure_ascii=False)}

    Επιστροφή σε JSON:
    {{
      "topics": ["topic1", "topic2", ...]
    }}
    """

    response = openai.ChatCompletion.create(
        engine=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": "Είσαι ειδικός στην περίληψη παρουσιάσεων."},
            {"role": "user", "content": prompt}
        ]
    )

    raw_content = response.choices[0].message["content"]
    parsed = extract_json(raw_content)
    return parsed.get("topics", [])

def get_embeddings(texts):
    response = openai.Embedding.create(
        input=texts,
        engine=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    )
    return [data['embedding'] for data in response['data']]

def check_consistency_dynamic(slides_text, similarity_threshold=0.75):
    topics = extract_main_topics(slides_text)
    topic_embeddings = get_embeddings(topics)

    issues = []
    for slide in slides_text:
        slide_text = slide['title'] + " " + " ".join(slide['content'])
        slide_embedding = get_embeddings([slide_text])[0]

        for topic, topic_emb in zip(topics, topic_embeddings):
            sim = cosine_similarity([slide_embedding], [topic_emb])[0][0]
            if sim < similarity_threshold:
                issues.append({
                    "slide_number": slide["slide_number"],
                    "missing_topic": topic,
                    "similarity_score": round(sim, 3)
                })

    return {"topics": topics, "issues": issues}