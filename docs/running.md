# Running and Testing the In-Memory Search Engine

## Step-by-Step Process

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run unit tests:
   ```
   python -m unittest discover -s tests
   ```
3. Execute the main application:
   ```
   python src/main.py
   ```
4. Start the API server (for integration testing):
   ```
   python -m uvicorn api.app:app
   ```
5. Verify outputs (for both CLI and API endpoints).
6. If everything works as expected, commit and push your changes.

# Running the Application

## Using Uvicorn
Run the application locally using Uvicorn:
```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000
```
Access the API at `http://127.0.0.1:8000`.

## Using Docker
1. **Build the Docker image:**
   ```bash
   docker build -t in-memory-search-engine .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 8000:8000 in-memory-search-engine
   ```

## Using Docker Compose
1. **Start the services:**
   ```bash
   docker-compose up --build
   ```

2. **Stop the services:**
   ```bash
   docker-compose down
   ```
