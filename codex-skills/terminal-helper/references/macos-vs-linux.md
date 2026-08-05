# macOS vs Linux Command Differences

## File Operations

| Task | Linux | macOS |
|------|-------|-------|
| List files | `ls` | `ls` (same) |
| Disk usage | `df -h` | `df -h` (same) |
| Dir size | `du -sh` | `du -sh` (same) |
| Find files | `find` | `find` (similar) |
| Locate | `locate` | `locate` (requires sudo) |

## System Commands

| Task | Linux | macOS |
|------|-------|-------|
| Package manager | `apt`, `yum`, `dnf` | `brew` |
| Update | `apt update && apt upgrade` | `brew update && brew upgrade` |
| Services | `systemctl` | `launchctl` |
| Process list | `ps aux` | `ps aux` (same) |
| Kill process | `kill` | `kill` (same) |
| Top | `top`, `htop` | `top`, `htop` |

## Networking

| Task | Linux | macOS |
|------|-------|-------|
| Config | `ip addr` | `ifconfig` or `ip` |
| Ping | `ping` | `ping` (same) |
| DNS | `/etc/resolv.conf` | `/etc/resolv.conf` (Catalina+) |

## Directory Structure

| Path | Linux | macOS |
|------|-------|-------|
| Home | `/home/user` | `/Users/user` |
| Temp | `/tmp` | `/tmp` or `$TMPDIR` |
| Config | `~/.config` | `~/Library/Application Support` |
| Logs | `/var/log` | `/var/log` or `~/Library/Logs` |

## Common Equivalents

| Linux | macOS | Notes |
|-------|-------|-------|
| `sudo apt install` | `brew install` | Package managers |
| `systemctl start` | `launchctl load` | Services |
| `systemctl status` | `launchctl list` | Service status |
| `ufw` | `pf` (firewall) | Different firewalls |
| `chmod +x` | `chmod +x` | Same |
| `chown` | `chown` | Same |

## Path Differences

```bash
# Linux
~/.config/opencode/
/var/log/syslog

# macOS
~/Library/Application Support/
/var/log/system.log  # Use Console app instead
```

## Package Managers

### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt upgrade
sudo apt install package
```

### macOS (Homebrew)
```bash
brew update
brew upgrade
brew install package
```

## Service Management

### Linux
```bash
systemctl start nginx
systemctl stop nginx
systemctl status nginx
```

### macOS
```bash
# Using launchctl
launchctl load /Library/LaunchAgents/com.nginx.plist
launchctl unload /Library/LaunchAgents/com.nginx.plist

# Using brew services (for brew-installed packages)
brew services start nginx
brew services stop nginx
```

## Disk & Filesystem

### Linux
```bash
df -h
mount
lsblk
```

### macOS
```bash
df -h
diskutil list
diskutil info /dev/disk1
```

## Shell

| Feature | Linux | macOS |
|---------|-------|-------|
| Default shell | `bash` or `zsh` | `zsh` (Catalina+) |
| Config file | `~/.bashrc` | `~/.zshrc` |
| Aliases | Same | Same |

## Useful macOS-Specific Commands

```bash
# Open file with default app
open file.txt

# Open URL
open https://example.com

# Reveal in Finder
open .

# Show hidden files
defaults write com.apple.finder AppleShowAllFiles YES
killall Finder

# Software update
softwareupdate -l
```

## Cross-Platform Scripts

```bash
# Detect OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "macOS"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Linux"
fi
```

## Environment Variables

| Linux | macOS |
|-------|-------|
| `$HOME` | `$HOME` (same) |
| `$USER` | `$USER` (same) |
| `$PATH` | `$PATH` (similar) |
| `$TMPDIR` | `$TMPDIR` (same) |
| `$HOSTNAME` | `$HOSTNAME` (same) |