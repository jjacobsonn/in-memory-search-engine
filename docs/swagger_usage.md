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

- **Inspect Responses:**  
  View the HTTP status codes, response body, and response headers directly within the UI. This helps you verify that:
  - The response status code matches your expectations.
  - The returned JSON structure (such as a list of search results) is correct.

- **Auto-generated Documentation Details:**  
  The Swagger UI displays:
  - Endpoint summaries and detailed descriptions.
  - Parameters (with examples and descriptions). For instance, the `prefix` parameter on `/autocomplete` is documented with an example like `"co"`.
  - Expected response models and example responses based on your Pydantic models.

## Benefits

Using Swagger UI provides a professional, interactive interface for:
- Quickly validating API behavior.
- Demonstrating endpoint functionality to team members and stakeholders.
- Troubleshooting issues by viewing full request/response details.

Use this guide to ensure that your API endpoints respond correctly and to streamline testing during development and staging.

Happy Testing!
