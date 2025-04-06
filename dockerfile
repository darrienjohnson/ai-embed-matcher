FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY ai_match_server.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "ai_match_server.py"]
