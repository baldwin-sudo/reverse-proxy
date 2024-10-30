# Proxy Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY backend.py .

RUN pip install Flask requests
EXPOSE  5000
CMD ["python", "backend.py"]
