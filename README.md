# In-Memory Search Engine

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green.svg)](https://fastapi.tiangolo.com/)
[![Makefile](https://img.shields.io/badge/Makefile-4.4%25-blue.svg)](https://github.com/jjacobsonn/in-memory-search-engine)
[![Dockerfile](https://img.shields.io/badge/Dockerfile-1.5%25-blue.svg)](https://github.com/jjacobsonn/in-memory-search-engine)
[![Build Status](https://github.com/jjacobsonn/in-memory-search-engine/actions/workflows/test.yml/badge.svg)](https://github.com/jjacobsonn/in-memory-search-engine/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/jjacobsonn/in-memory-search-engine.svg)](https://github.com/jjacobsonn/in-memory-search-engine/stargazers)
[![Watchers](https://img.shields.io/github/watchers/jjacobsonn/in-memory-search-engine.svg)](https://github.com/jjacobsonn/in-memory-search-engine/watchers)
[![Forks](https://img.shields.io/github/forks/jjacobsonn/in-memory-search-engine.svg)](https://github.com/jjacobsonn/in-memory-search-engine/network/members)
[![Releases](https://img.shields.io/github/release/jjacobsonn/in-memory-search-engine.svg)](https://github.com/jjacobsonn/in-memory-search-engine/releases)


A high-performance in-memory search engine using realistic search data inspired by daily software engineering tasks. The API provides both advanced autocomplete and fuzzy search endpoints, returning detailed metadata.

## Features
- **Autocomplete Search:** Fast prefix-based search using a Trie data structure.
- **Fuzzy Search:** Typo-tolerant search using Levenshtein distance.
- **Detailed Metadata:** Execution time, algorithm used, and more.

## Live Demo
Check out the live demo: [In-Memory Search Engine](https://in-memory-search-engine.onrender.com/)

## Table of Contents
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Documentation](#documentation)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/jjacobsonn/in-memory-search-engine.git
   cd in-memory-search-engine
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
### Using Uvicorn
Run the application locally using Uvicorn:
```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000
```
Access the API at `http://127.0.0.1:8000`.

### Using Docker
1. **Build the Docker image:**
   ```bash
   docker build -t in-memory-search-engine .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 8000:8000 in-memory-search-engine
   ```

### Using Docker Compose
1. **Start the services:**
   ```bash
   docker-compose up --build
   ```

2. **Stop the services:**
   ```bash
   docker-compose down
   ```

## Testing
Run the tests using `pytest`:
```bash
pytest --maxfail=1 --disable-warnings -v
```

## Deployment
Refer to the [Deployment Guide](docs/deployment.md) for detailed deployment instructions.

## Contributing
We welcome contributions! Please see our [Contributing Guide](docs/CONTRIBUTING.md) for more details.

## Documentation
- [Curl Usage Guide](docs/curl_usage.md)
- [Advanced Features](docs/advanced_features.md)
- [System Overview](docs/system_overview.md)
- [Running the Application](docs/running.md)
- [Staging Deployment](docs/staging_deployment.md)
- [Swagger Usage](docs/swagger_usage.md)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Additional Resources
- **GitHub Actions:** [View all workflows](https://github.com/jjacobsonn/in-memory-search-engine/actions)
- **Releases:** [View all releases](https://github.com/jjacobsonn/in-memory-search-engine/releases)
