# Docker Command Reference

## Container Operations

| Command | Description | Example |
|---------|-------------|---------|
| `docker run` | Start container | `docker run -d nginx` |
| `docker ps` | List running containers | `docker ps` |
| `docker ps -a` | List all containers | `docker ps -a` |
| `docker stop` | Stop container | `docker stop container_id` |
| `docker start` | Start container | `docker start container_id` |
| `docker restart` | Restart container | `docker restart container_id` |
| `docker rm` | ⚠️ Remove container | `docker rm container_id` |

## Image Operations

| Command | Description | Example |
|---------|-------------|---------|
| `docker images` | List images | `docker images` |
| `docker pull` | Download image | `docker pull nginx:latest` |
| `docker rmi` | ⚠️ Remove image | `docker rmi image_id` |
| `docker build` | Build from Dockerfile | `docker build -t myapp .` |
| `docker tag` | Tag image | `docker tag myapp myrepo/myapp:v1` |

## Common Flags

| Flag | Purpose | Example |
|------|---------|---------|
| `-d` | Detached mode | `docker run -d` |
| `-p` | Port mapping | `docker run -p 8080:80` |
| `-v` | Volume mount | `docker run -v /data:/data` |
| `-e` | Environment var | `docker run -e ENV=prod` |
| `--name` | Container name | `docker run --name myapp` |
| `--rm` | Auto-remove on exit | `docker run --rm` |

## Networking

| Command | Description |
|---------|-------------|
| `docker network ls` | List networks |
| `docker network create` | Create network |
| `docker network inspect` | View network details |

## Volumes

| Command | Description |
|---------|-------------|
| `docker volume ls` | List volumes |
| `docker volume create` | Create volume |
| `docker volume rm` | ⚠️ Remove volume |

## Logs & Debugging

| Command | Description |
|---------|-------------|
| `docker logs` | View container logs |
| `docker logs -f` | Follow logs |
| `docker exec` | Run command in container |
| `docker inspect` | Container details |

## Docker Compose

| Command | Description |
|---------|-------------|
| `docker-compose up` | Start services |
| `docker-compose up -d` | Detached |
| `docker-compose down` | Stop services |
| `docker-compose ps` | List services |
| `docker-compose logs` | View logs |

## ⚠️ Dangerous Commands

- `docker system prune` - Cleans up resources
- `docker rm -f $(docker ps -aq)` - Kills ALL containers
- `docker rmi -f $(docker images -q)` - Removes ALL images
- `docker volume prune` - Removes unused volumes

## Best Practices

1. **Always name containers** - Use `--name`
2. **Use volumes for persistence** - Don't store in container
3. **Use networks for communication** - Container-to-container
4. **Check logs first** - `docker logs container_id`
5. **Use docker-compose** - For multi-container apps