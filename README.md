# In-Memory Search Engine

This project implements an efficient trie-based search engine with support for autocomplete and fuzzy search. It is designed for rapid lookups and correction of typos.

## Features
- **Trie-Based Indexing:** Fast insertion and lookup for autocomplete.
- **Fuzzy Search:** Uses techniques like Levenshtein distance to handle typos.
- **Efficient Memory Use:** Optimized for performance in memory-sensitive applications.

## Repository Structure
- **src/**: Contains the core implementation (trie and fuzzy search logic).
- **tests/**: Unit and integration tests to ensure correctness.

## Getting Started
1. Clone the repository.
2. Install dependencies (e.g., via `pip install -r requirements.txt` for Python).
3. Run the project with `python src/main.py`.

## Next Steps
- Run unit tests: `python -m unittest discover -s tests`
- Verify output from `src/main.py`
- Commit and push changes once confirmed

## License
This project is licensed under the MIT License.
