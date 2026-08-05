# Security Audit Checklist

## Before Any Operation

- [ ] Understood what the command does
- [ ] Verified it only affects intended files
- [ ] Checked file permissions first
- [ ] Backed up important data
- [ ] Understood all flags used
- [ ] No credentials in command
- [ ] Logged operation in MEMORY.md

## File Permission Checks

### Sensitive Files (Should be 600 or 400)
```bash
ls -la ~/.ssh/
ls -la ~/.git-credentials
ls -la ~/.netrc
```

### World-Writable (Security Risk)
```bash
find ~ -type f -perm -002
```

### SUID Files (Potential Exploit)
```bash
find / -type f -perm /4000 2>/dev/null
```

## Network Security

### Check Open Ports
```bash
netstat -tuln | grep LISTEN
```

### SSH Security
```bash
# Check SSH config
sshd -t

# Verify key permissions
ls -la ~/.ssh/*.pub
```

## User Security

### Check sudo access
```bash
sudo -l
```

### Failed login attempts
```bash
lastb -n 10
```

## Recommendations

1. Use SSH keys instead of passwords
2. Disable root login via SSH
3. Use fail2ban for brute force protection
4. Keep system updated
5. Review logs regularly
6. Use firewall (ufw/firewalld)