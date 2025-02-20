# In-Memory Search Engine

This project implements an efficient, in-memory search engine featuring:
- **Trie-based Autocomplete:** Offers fast prefix lookup.
- **Fuzzy Search:** Uses Levenshtein distance (with an accelerated C-based fallback if available) to handle typos and provide near-match suggestions.

## Features
- Fast, memory-efficient search using a trie data structure.
- Robust fuzzy search to correct minor misspellings.
- Easy-to-run tests and a main application demonstrating core functionality.

## Getting Started

### Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure you are using Python 3 (use `python3` if needed).

### Running the Application
Run the main application:
   ```bash
   python3 src/main.py
   ```

### Running Tests
Validate functionality with unit tests:
   ```bash
   python3 -m unittest discover -s tests
   ```

## Documentation
- [Design Document](docs/design.md): Overview of the system architecture.
- [Running Instructions](docs/running.md): Detailed steps to run and test the project.
- [Next Steps](docs/next_steps.md): Future improvements and roadmap.
- [Contributing](docs/CONTRIBUTING.md): Guidelines for contributing to the project.

## License
This project is licensed under the MIT License.
