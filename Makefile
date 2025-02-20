.PHONY: install test run docker-build docker-run clean

# Install dependencies
install:
	@echo "Installing dependencies..."
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

# Run unit & integration tests with API server
test:
	@echo "Starting API server in background..."
	nohup python3 -m uvicorn api.app:app --host 127.0.0.1 --port 8000 > /dev/null 2>&1 &
	@sleep 5
	@echo "Running tests..."
	pytest --maxfail=1 --disable-warnings -v
	@echo "Killing API server..."
	@pkill -f "uvicorn"

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
