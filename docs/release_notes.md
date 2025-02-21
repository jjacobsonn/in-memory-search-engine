# Release Notes v1.0.0

## Overview
- High-performance in-memory search engine with trie-based autocomplete and fuzzy search (Levenshtein distance).
- API built with FastAPI and uvicorn.

## Features
- **Autocomplete**: Fast prefix lookup via trie.
- **Fuzzy Search**: Spell-correction using an accelerated Levenshtein algorithm.
- **API Endpoints**: 
  - `/autocomplete?prefix=...`
  - `/fuzzy?query=...&max_distance=...`

## Installation
1. Clone the repository.
2. Run:
   ```bash
   make install
   ```
3. Test with:
   ```bash
   make test
   ```

## Usage
- Launch the main application:
   ```bash
   make run
   ```
- For API access, visit http://127.0.0.1:8000/docs
- Docker users:
   ```bash
   make docker-build
   make docker-run
   ```

## Deployment
- Follow [docs/deployment.md](docs/deployment.md) for staging/production deployment and monitoring.

## Future Improvements
- Enhanced logging, monitoring, and authentication.
- Performance benchmarks and stress testing.
