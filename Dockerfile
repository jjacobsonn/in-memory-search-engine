FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose API port
EXPOSE 8000

# Default command to start API server (FastAPI with uvicorn)
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
