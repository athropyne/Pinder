FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install debugpy
COPY . .
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app
CMD ["python", "main.py"]