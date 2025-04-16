
# 🧠 ai-embed-matcher

This is the **AI-powered microservice** used in the [AI Job Matcher](https://github.com/YOUR_USERNAME/ai-job-matcher) platform. It provides a REST API that compares a candidate's resume to job descriptions and returns a **semantic similarity score** — powered by `sentence-transformers`.

---

## 🚀 Features

- 🧩 Converts resume + job description into **vector embeddings**
- ⚡ Uses [`all-MiniLM-L6-v2`](https://www.sbert.net/docs/pretrained_models.html) for fast and accurate scoring
- 📏 Returns a **cosine similarity score** between `0.0` (no match) and `1.0` (perfect match)
- 🐳 Fully containerized with Docker for easy deployment

---

## 📦 API Endpoint

### `POST /similarity`

**Request:**
```json
{
  "resume": "Experienced backend engineer skilled in Java and Spring Boot.",
  "job": "Looking for a Java backend developer familiar with Spring Boot."
}
Response:

{
  "similarity": 0.85
}
🔗 Part of a Larger System

This microservice is one of three core components in the AI Job Matcher system:


Component	Description
🧠 ai-embed-matcher	This Python microservice for similarity scoring
🔧 ai-job-matcher	Java Spring Boot backend API + database
💻 ai-job-matcher-frontend	Next.js frontend for user interaction
👉 See Full System Architecture in ai-job-matcher

🛠️ Getting Started

1. Clone the repo
git clone https://github.com/YOUR_USERNAME/ai-embed-matcher.git
cd ai-embed-matcher
2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run the server
python server.py
Your API will be available at:
📍 http://localhost:5001/similarity

🐳 Docker Support (Optional)

To build and run the microservice using Docker:

docker build -t ai-embed-matcher .
docker run -p 5001:5001 ai-embed-matcher
🧠 Tech Stack

Python 3.9+
Flask
sentence-transformers
Cosine similarity
Docker (optional)
💬 Questions or Ideas?

This project was built by Darrien Johnson as part of an AI-powered job matching platform.
Feel free to fork, contribute, or reach out with suggestions!


---

Let me know if you want me to create a matching version for your `ai-job-matcher` backend repo too!