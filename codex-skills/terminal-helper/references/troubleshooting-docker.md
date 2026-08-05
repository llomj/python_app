# Docker Troubleshooting Guide

## Common Issues & Solutions

### Container Won't Start

**Diagnosis**:
```bash
docker ps -a
docker logs container_name
docker inspect container_name
```

**Solutions**:
1. Check logs: `docker logs container_id`
2. Check port: `docker port container_id`
3. Check env vars: `docker inspect container_id | grep -i env`

### Network Issues

**Diagnosis**:
```bash
docker network ls
docker network inspect network_name
docker exec container_id ping other_container
```

**Solutions**:
1. Create network: `docker network create mynet`
2. Connect: `docker network connect mynet container_id`
3. Check DNS: `docker exec container_id nslookup service`

### Volume Mount Not Working

**Diagnosis**:
```bash
docker inspect container_id | grep -A 10 Mounts
ls -la /path/on/host
```

**Solutions**:
1. Check path exists on host
2. Use absolute paths
3. Check permissions: `chmod 777 path`

### Out of Space

**Diagnosis**:
```bash
docker system df
docker images
docker ps -s
```

**Solutions**:
```bash
# Clean up
docker system prune -a
docker container prune
docker image prune -a
docker volume prune
```

### Permission Denied in Container

**Diagnosis**:
```bash
docker exec container_id id
docker exec container_id ls -la /app
```

**Solutions**:
1. Use user in Dockerfile: `USER 1000:1000`
2. Fix host permissions: `chmod -R 755 /host/path`
3. Use named volume instead of bind mount

### Image Not Found

**Diagnosis**:
```bash
docker images
docker search image_name
```

**Solutions**:
1. Pull image: `docker pull image_name:tag`
2. Check tag: `docker images | grep image`
3. Build locally: `docker build -t name .`

### Port Already in Use

**Diagnosis**:
```bash
netstat -tulpn | grep PORT
docker ps
```

**Solutions**:
1. Use different port: `-p 8081:80`
2. Stop conflicting container: `docker stop container_id`
3. Kill process: `kill $(lsof -t -i:PORT)`

### Container Exits Immediately

**Diagnosis**:
```bash
docker logs container_id
docker inspect container_id
```

**Solutions**:
1. Check exit code: `docker wait container_id`
2. Keep container running: `docker run -d your_image tail -f /dev/null`
3. Fix CMD/ENTRYPOINT in Dockerfile

## Diagnostic Commands

| Issue | Command |
|-------|---------|
| Container issues | `docker ps -a` |
| Image issues | `docker images` |
| Network issues | `docker network ls` |
| Volume issues | `docker volume ls` |
| Disk usage | `docker system df` |
| Logs | `docker logs -f container` |

## Logs Debugging

```bash
# All containers
docker logs container_id

# Follow mode
docker logs -f container_id

# Last 100 lines
docker logs --tail 100 container_id

# Timestamps
docker logs -t container_id

# Since time
docker logs --since 1h container_id
```

## Health Check

```bash
# Container health
docker inspect --format='{{.State.Health.Status}}' container_id

# Stats
docker stats --no-stream

# Top processes in container
docker top container_id
```

## Reset Docker

```bash
# Danger! Removes everything
docker system prune -a --volumes --rmi all
```