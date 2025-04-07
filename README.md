🧠 AI Job Matching Microservice
This microservice provides AI-powered similarity scoring between resumes and job descriptions using SentenceTransformers. It exposes a REST API that takes in text from a candidate's resume and a job posting, then returns a cosine similarity score based on semantic meaning — not just keywords.

🚀 Features
Converts resume + job description into vector embeddings

Uses all-MiniLM-L6-v2 model for high-speed, high-accuracy scoring

Returns a score between 0.0 (no match) and 1.0 (perfect match)

Fully containerized with Docker