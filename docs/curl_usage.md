# Curl Usage Guide for API Endpoint Verification

This guide provides example curl commands to test the deployed API endpoints and confirms that the correct HTTP status codes and response payloads are returned.

## Prerequisites
- The API must be deployed on your staging environment (e.g., `https://staging.example.com`).
- Ensure the endpoints are running and accessible via the internet.

## Testing the Autocomplete Endpoint

Run the following command to test the autocomplete endpoint:
```bash
curl -i "https://staging.example.com/autocomplete?prefix=de"
```
**Expected outcome:**
- **HTTP Status Code:** 200 if matches are found, or 404 if no data exists for the given prefix.
- **Response Body (Sample):**
  ```json
  {
    "results": ["debug", "deployment"]
  }
  ```
  If no matches exist, you should see:
  ```json
  {
    "detail": "No matches found"
  }
  ```

## Testing the Fuzzy Search Endpoint

Run this command to test the fuzzy endpoint:
```bash
curl -i "https://staging.example.com/fuzzy?query=cod%20revie&max_distance=2"
```
**Notes:**
- Use URL encoding for any spaces (e.g., `cod revie` becomes `cod%20revie`).
  
**Expected outcome:**
- **HTTP Status Code:** 200 if near-matches are found, or 404 if no near matches found.
- **Response Body (Sample):**
  ```json
  {
    "results": ["code review"]
  }
  ```
  Otherwise, a 404 response with an appropriate error message.

## Troubleshooting

- **If you receive a non-200 status code:**  
  Verify that the staging URL is correct and the API is running. Also check that your curl command is correctly formed with URL-encoded parameters.

- **If the response body is not as expected:**  
  Compare the output with your demo data to ensure that the query parameters produce the proper results based on realistic examples.

Using these curl commands provides a professional and automated way to verify API functionality in your staging environment.
