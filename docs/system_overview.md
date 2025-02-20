# System Overview & Workflow

This project provides a high-performance in-memory search engine with autocomplete and fuzzy search capabilities.

## Core Components
1. **Trie Data Structure (src/trie.py)**  
   - Powers the fast autocomplete feature by indexing words in a tree for quick prefix lookups.

2. **Fuzzy Search (src/fuzzy_search.py)**  
   - Implements edit-distance based matching to handle typos or near matches.

3. **Demo Data (data/demo_data.json)**  
   - Supplies realistic software engineering terms (e.g., "debug," "deployment") so users can test autocomplete/fuzzy search with real-world examples.

4. **API Layer (api/app.py)**  
   - FastAPI application exposing two major endpoints:
     - /autocomplete: Returns terms matching a specified prefix.
     - /fuzzy: Returns near matches for a possibly misspelled query.

## How to Run Locally
1. **Install Dependencies:**  
   ```bash
   make install
   ```
2. **Run Tests (Optional):**  
   ```bash
   make test
   ```
   This ensures the endpoints and core logic work as expected.
3. **Start the API:**  
   ```bash
   make run
   ```
   By default, FastAPI serves on http://127.0.0.1:8000.  
   - Go to http://127.0.0.1:8000/docs to see the Swagger UI.
   - Test endpoints using /autocomplete and /fuzzy queries.

## How to Run with Docker
1. **Build the Docker Image:**  
   ```bash
   make docker-build
   ```
2. **Run the Container:**  
   ```bash
   make docker-run
   ```
   This starts your API in a container, also on port 8000.

## What the Application Does
- **Autocomplete:** Quickly finds terms beginning with a user-supplied prefix.  
  Example: prefix = "co" → ["commit", "code review", "container"]
- **Fuzzy Search:** Returns terms similar to the query based on a maximum allowed edit distance.  
  Example: query = "cod revie", max_distance=2 → ["code review"]

## Key Benefits
- **High Performance:** In-memory data structures reduce latency in lookups.
- **Realistic Data:** The pre-populated demo data mimics typical software engineering jargon.
- **Ease of Testing:** Swagger UI or simple curl commands let you see immediate results.
- **Extensibility:** You can add more terms, switch data structures, or enhance fuzzy matching as needed.

This overview should help you understand how to install, run, and test the application, as well as clarify what the search engine does under the hood.
