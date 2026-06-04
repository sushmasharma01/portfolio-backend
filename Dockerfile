FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (important for psycopg2)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Environment
ENV PYTHONUNBUFFERED=1

# Start app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "10000"]