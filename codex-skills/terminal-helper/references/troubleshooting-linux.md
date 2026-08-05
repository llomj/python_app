# Linux Troubleshooting Guide

## Common Issues & Solutions

### System Won't Boot

**Symptoms**: Machine doesn't start

**Diagnosis**:
```bash
# Check last boot logs
journalctl -b -1

# Check disk space
df -h

# Check filesystem
fsck /dev/sda1
```

**Solutions**:
1. Boot in recovery mode
2. Check disk for errors
3. Verify fstab entries

### High CPU Usage

**Diagnosis**:
```bash
top
htop
ps aux --sort=-%cpu | head -10
```

**Solutions**:
1. Identify process: `ps -p <pid>`
2. Check if legitimate: `ls -l /proc/<pid>/exe`
3. Kill if malicious: `kill -9 <pid>`

### Out of Disk Space

**Diagnosis**:
```bash
df -h
du -sh /*
du -sh /var/*
```

**Solutions**:
1. Clear logs: `sudo journalctl --vacuum-time=7d`
2. Clean apt: `sudo apt autoremove`
3. Find large files: `find / -type f -size +100M`

### Network Not Working

**Diagnosis**:
```bash
ip addr
ip route
ping 8.8.8.8
nslookup google.com
```

**Solutions**:
1. Restart network: `sudo systemctl restart NetworkManager`
2. Check DNS: `cat /etc/resolv.conf`
3. Reset interface: `sudo ip link set eth0 down && up`

### Permission Denied

**Diagnosis**:
```bash
ls -la /path/to/file
id
groups
```

**Solutions**:
1. Add to group: `sudo usermod -aG group $USER`
2. Change owner: `sudo chown user:group file`
3. Change permissions: `chmod 644 file`

### Service Won't Start

**Diagnosis**:
```bash
sudo systemctl status service-name
sudo journalctl -u service-name -n 50
```

**Solutions**:
1. Check config: `sudo systemctl cat service-name`
2. Check logs: `journalctl -xe`
3. Restart: `sudo systemctl restart service-name`

### SSH Connection Failed

**Diagnosis**:
```bash
ssh -v user@host
sudo systemctl status sshd
```

**Solutions**:
1. Check key permissions: `ls -la ~/.ssh/`
2. Verify host key: `ssh-keygen -R hostname`
3. Check firewall: `sudo ufw status`

## Diagnostic Commands

| Issue | Command |
|-------|---------|
| Memory | `free -h` |
| CPU | `top` or `htop` |
| Disk | `df -h` |
| Processes | `ps aux` |
| Network | `ss -tuln` |
| Logs | `journalctl -xe` |
| Services | `systemctl list-units --failed` |

## Quick Health Check

```bash
# Run system diagnostics
echo "=== System Health ==="
echo "Uptime: $(uptime)"
echo "Load: $(cat /proc/loadavg)"
echo "Memory: $(free -h | grep Mem)"
echo "Disk: $(df -h / | tail -1)"
echo "Failed Services: $(systemctl --failed --no-pager | tail -1)"
```