# FROM arm64v8/python:3.11.4-slim-bullseye as base
FROM arm64v8/python:3.11-alpine
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0", "--port", "5002"]
