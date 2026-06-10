# flask-server-devops
# FlaskWebApp-Devops

## CI/CD secrets

Add these secrets in GitHub Actions:

- `DOCKER_USERNAME`: Docker Hub username, used to tag, push, and pull the image.
- `DOCKER_PASSWORD`: Docker Hub password or personal access token, used by GitHub Actions to push the image.
- `VM_HOST`: VM public IP or DNS name, used by the SSH deploy step.
- `VM_USER`: VM SSH username, for example `azureuser`.
- `VM_SSH_KEY`: private SSH key content from the `.pem` file, used by the SSH deploy step.

## Docker image

Build locally:

```bash
docker build -t my-app .
```

Push manually:

```bash
docker login
docker tag my-app:latest <dockerhub-username>/my-app:latest
docker push <dockerhub-username>/my-app:latest
```
