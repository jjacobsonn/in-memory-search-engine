# In-Memory Search Engine

A high-performance search engine featuring trie-based autocomplete and fuzzy search (Levenshtein distance), exposed via a FastAPI service.

## Quick Start
1. Install:  
   ```bash
   pip install -r requirements.txt
   ```
2. Test:  
   ```bash
   python -m unittest discover -s tests
   ```
3. Run:  
   - Main app: `python src/main.py`  
   - API server: `python -m uvicorn api.app:app`

## Architecture
- **Core Engine:** Trie and fuzzy search algorithms.
- **API Layer:** Real-time endpoints powered by FastAPI.
- **Testing:** Unit and integration tests ensure reliability.

## Deployment & Contributing
- See [docs/deployment.md](docs/deployment.md) for deployment guidelines.
- Review [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for contribution instructions.

## License
MIT License
