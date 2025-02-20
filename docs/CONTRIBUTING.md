# Contributing to In-Memory Search Engine

## Getting Started
- Ensure you run all tests (unit and integration):  
  `pytest --maxfail=1 --disable-warnings -v`
- Verify functionality via `uvicorn api.app:app --host 0.0.0.0 --port 8000`.

## How to Contribute
- Fork the repository and create a new branch for your changes.
- Follow the coding standards as specified in our design documentation.
- Include tests for both core functionality and API endpoints.
- Commit with clear messages and push your changes for review.

## Next Steps for Development
- Integrate Continuous Integration (CI) for automated testing.
- Enhance documentation with new features and API usage examples.
- Optimize performance and add further unit and integration tests.
