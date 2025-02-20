# Staging Deployment Guide

This guide explains how to automatically deploy your In-Memory Search Engine API to a staging environment using Docker and GitHub Actions.

## Prerequisites
- A Docker Hub (or similar) account.
- A staging server with Docker and Docker Compose installed.
- SSH access and environment variables set up on the staging server.
- GitHub Actions configured for CI/CD in your repository.

## Step 1: Build & Tag the Docker Image
Build the Docker image with a staging tag:
```bash
docker build -t yourdockerhubusername/in-memory-search-engine:staging .
```

## Step 2: Push the Image to Docker Hub
Log in to Docker Hub and push the image:
```bash
docker push yourdockerhubusername/in-memory-search-engine:staging
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
          docker build -t yourdockerhubusername/in-memory-search-engine:staging .
          echo "$DOCKERHUB_PASSWORD" | docker login --username "$DOCKERHUB_USERNAME" --password-stdin
          docker push yourdockerhubusername/in-memory-search-engine:staging
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
- GitHub Actions takes care of deploying to your staging environment.
- You can easily verify the full API functionality on your staging server.

Use this guide to streamline your deployment process and bring your project production-ready in a professional, open source manner.
