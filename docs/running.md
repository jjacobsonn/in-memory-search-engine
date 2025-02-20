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
