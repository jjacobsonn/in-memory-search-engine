# Swagger UI Usage Guide

The In-Memory Search Engine API provides an auto-generated Swagger UI, which makes it easy to interact with and test the API endpoints without writing any code.

## How to Access the Swagger UI

1. **Deploy the API:**  
   Ensure your API is deployed. For example, if running locally, start the API:
   ```bash
   python -m uvicorn api.app:app --host 127.0.0.1 --port 8000
   ```
   If deployed to staging, use the appropriate URL (e.g., `https://staging.example.com`).

2. **Open the Swagger UI in Your Browser:**  
   - **Local Deployment:** Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **Staging Deployment:** Navigate to `https://staging.example.com/docs`

## What You Can Do in the Swagger UI

- **View Endpoints:**  
  See a list of available endpoints (e.g., `/autocomplete` and `/fuzzy`) with detailed descriptions.
  
- **Interactive Testing:**  
  - Click on any endpoint to expand its details.
  - Fill in parameter fields with examples (or your own test values). For example, try entering `"co"` for the prefix in the `/autocomplete` endpoint.
  - Click the **Execute** button to send a request.

## Example Tests

### Autocomplete Endpoint

**Description:** Returns a list of search terms that begin with the provided prefix based on realistic demo data.

**Example Request:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/autocomplete?prefix=co' \
  -H 'accept: application/json'
```

**Expected Response:**
- **HTTP Status Code:** 200 if matches are found, or 404 if no data exists for the given prefix.
- **Response Body (Sample):**
  ```json
  {
    "results": ["commit", "code review", "container"]
  }
  ```
  If no matches exist, you should see:
  ```json
  {
    "detail": "No matches found"
  }
  ```

### Fuzzy Search Endpoint

**Description:** Returns near-matching search terms for typos in the query string using a Levenshtein algorithm.

**Example Request:**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/fuzzy?query=cod%20revie&max_distance=2' \
  -H 'accept: application/json'
```

**Expected Response:**
- **HTTP Status Code:** 200 if near-matches are found, or 404 if no near matches found.
- **Response Body (Sample):**
  ```json
  {
    "results": ["code review"]
  }
  ```
  Otherwise, a 404 response with an appropriate error message.

## Benefits

Using Swagger UI provides a professional, interactive interface for:
- Quickly validating API behavior.
- Demonstrating endpoint functionality to team members and stakeholders.
- Troubleshooting issues by viewing full request/response details.

Use this guide to ensure that your API endpoints respond correctly and to streamline testing during development and staging.

Happy Testing!
