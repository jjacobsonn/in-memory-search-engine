# Staging Deployment Guide

## Pre-deployment
- Ensure all tests pass: `pytest --maxfail=1 --disable-warnings -v`
- Review the CI/CD pipeline in .github/workflows/test.yml

## Deployment Steps
1. Commit and push changes to the remote repository.
2. Deploy the API to a staging server:
   - Run: `uvicorn api.app:app --host 0.0.0.0 --port 8000` on the staging environment.
3. Verify that all API endpoints function as expected using tools like Postman.
4. Monitor logs and performance; update monitoring configurations if needed.

## Post-deployment
- Gather feedback and monitor performance metrics.
- Plan iterative improvements based on usage and performance.

## Prerequisites
- A Docker Hub account.
- A staging server with Docker and Docker Compose installed.
- SSH access and proper environment variables set on the staging server.
- GitHub Actions configured for CI/CD in your repository.

## Step 1: Build & Tag the Docker Image
Build the Docker image with a staging tag:
```bash
docker build -t jjacobsonn/in-memory-search-engine:staging .
```

## Step 2: Push the Image to Docker Hub
Log in to Docker Hub and push the image:
```bash
docker push jjacobsonn/in-memory-search-engine:staging
```

## Step 3: Configure Staging Deployment via GitHub Actions
Add a GitHub Actions workflow (e.g., `.github/workflows/deploy_staging.yml`) that:
- Checks out the repository.
- Builds the Docker image.
- Pushes the image to Docker Hub.
- SSHs to the staging server and runs `docker-compose pull` followed by `docker-compose up -d` to update the running service.

Example snippet:
```yaml
# filepath: /Users/cjacobson/git/in-memory-se/.github/workflows/deploy_staging.yml
name: Deploy to Staging

on:
  push:
    branches: [ "staging" ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build and push Docker image
        run: |
          docker build -t jjacobsonn/in-memory-search-engine:staging .
          echo "$DOCKERHUB_PASSWORD" | docker login --username "$DOCKERHUB_USERNAME" --password-stdin
          docker push jjacobsonn/in-memory-search-engine:staging
      - name: Deploy to staging server
        uses: appleboy/ssh-action@v0.1.7
        with:
          host: ${{ secrets.STAGING_HOST }}
          username: ${{ secrets.STAGING_USER }}
          key: ${{ secrets.STAGING_SSH_KEY }}
          script: |
            cd /path/to/your/docker-compose-directory
            docker-compose pull
            docker-compose up -d
```

## Step 4: Test the Deployed Endpoints
After deploying, verify that the staging URL (e.g., `https://staging.example.com`) works as expected:
- Visit `https://staging.example.com/docs` for the Swagger UI, or
- Use curl:
  ```bash
  curl "https://staging.example.com/autocomplete?prefix=appl"
  curl "https://staging.example.com/fuzzy?query=helo&max_distance=2"
  ```

## Summary
This automated process ensures that:
- Your project is built, tagged, and pushed using Docker.
- GitHub Actions handles deployment to your staging environment.
- You can easily verify full API functionality on your staging server.

## Additional Resources
- **GitHub Actions:** [View all workflows](https://github.com/jjacobsonn/in-memory-search-engine/actions)
- **Releases:** [View all releases](https://github.com/jjacobsonn/in-memory-search-engine/releases)
