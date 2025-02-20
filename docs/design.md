# In-Memory Search Engine Design Document

## 1. High-Level Architectural Overview
The system consists of three major layers:
- **Core Search Engine:** 
  - Autocomplete using a trie data structure.
  - Fuzzy search for typo correction using Levenshtein distance.
- **API Layer:** 
  - Exposes endpoints (via FastAPI) for autocomplete and fuzzy search.
- **Integration & Testing:** 
  - Integration tests ensure the API behaves as expected.

### System Diagram:
     +-----------------------+
     |      main.py          |
     +-----------+-----------+
                 |
     +-----------v-----------+
     |  Core Search Engine   | <--- Includes trie.py and fuzzy_search.py
     +-----------+-----------+
                 |
     +-----------v-----------+
     |      API Layer        | <--- Exposes endpoints via FastAPI (api/app.py)
     +-----------------------+
                 |
       [Data Source: In-memory dataset]

## 2. Implementation Details
- **Trie for Autocomplete:**  
   - Stores strings for fast prefix lookup.
   - Each node contains children mapped by characters and flags for end-of-word.
- **Fuzzy Search:**  
   - Uses a dynamic programming solution with an accelerated fallback using python-Levenshtein.
- **API Layer:**  
   - Implements endpoints for `/autocomplete` and `/fuzzy` using FastAPI.
- **Testing:**  
   - Combination of unit tests and integration tests ensures reliability.