# In-Memory Search Engine

A high-performance search engine featuring trie-based autocomplete and fuzzy search (Levenshtein distance), exposed via a FastAPI service.

## Quick Start

### Local Installation & Testing
1. Install dependencies:
   ```bash
   make install
   ```
2. Run tests:
   ```bash
   make test
   ```
3. Run the main application or API server:
   ```bash
   make run
   ```

### Docker Usage
1. Build the Docker image:
   ```bash
   make docker-build
   ```
2. Start the container:
   ```bash
   make docker-run
   ```

## Architecture
- **Core Engine:** Trie and fuzzy search algorithms.
- **API Layer:** Real-time endpoints powered by FastAPI.
- **Testing:** Unit and integration tests ensure reliability.

## Deployment & Contributing
- See [docs/deployment.md](docs/deployment.md) for deployment guidelines.
- Review [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for contribution instructions.

## License
MIT License
