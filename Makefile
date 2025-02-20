.PHONY: install test run docker-build docker-run clean

# Install dependencies
install:
	@echo "Installing dependencies..."
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

# Run unit & integration tests
test:
	@echo "Running tests..."
	python3 -m unittest discover -s tests

# Run main application and API
run:
	@echo "Starting main application..."
	python3 src/main.py
	@echo "Starting API server..."
	python3 -m uvicorn api.app:app

# Build Docker image
docker-build:
	@echo "Building Docker image..."
	docker build -t in-memory-search-engine .

# Run using docker-compose
docker-run:
	@echo "Starting Docker container..."
	docker-compose up

# Clean up temporary files
clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
