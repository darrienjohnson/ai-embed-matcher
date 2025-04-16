print(f"🔎 Running file directly? __name__ = {__name__}")

from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util

print("💡 File loaded")

# 🔧 Initialize Flask
app = Flask(__name__)

# 🧠 Load sentence transformer model
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

if __name__ == "__main__":
    print("✅ RUNNING THE SERVER on http://localhost:5000 🚀")
    app.run(host="0.0.0.0", port=5001, debug=True)