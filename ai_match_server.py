from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/similarity', methods=['POST'])
def compute_similarity():
    data = request.get_json()
    resume = data.get("resume", "")
    job = data.get("job", "")

    if not resume or not job:
        return jsonify({"error": "Missing resume or job text"}), 400

    embeddings = model.encode([resume, job], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1]).item()

    return jsonify({"similarity": score})
