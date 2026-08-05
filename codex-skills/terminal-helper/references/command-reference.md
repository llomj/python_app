# Terminal Command Reference

## Navigation

| Command | Description | Example |
|---------|-------------|---------|
| `ls` | List directory contents | `ls -la` |
| `cd` | Change directory | `cd /home/user` |
| `pwd` | Print working directory | `pwd` |
| `pushd` | Push directory to stack | `pushd /tmp` |
| `popd` | Pop directory from stack | `popd` |
| `tree` | Display directory tree | `tree -L 2` |

## File Operations

| Command | Description | Example |
|---------|-------------|---------|
| `cp` | Copy files | `cp file.txt backup.txt` |
| `mv` | Move/rename | `mv old.txt new.txt` |
| `mkdir` | Create directory | `mkdir newfolder` |
| `touch` | Create empty file | `touch file.txt` |
| `rm` | Remove (use caution) | `rm file.txt` |
| `ln` | Create link | `ln -s source link` |

## Viewing Files

| Command | Description | Example |
|---------|-------------|---------|
| `cat` | Display contents | `cat file.txt` |
| `less` | Page through | `less large.txt` |
| `head` | View start | `head -20 file.txt` |
| `tail` | View end | `tail -20 file.txt` |
| `grep` | Search in files | `grep "pattern" file` |

## System Info

| Command | Description | Example |
|---------|-------------|---------|
| `top` | Process monitor | `top` |
| `htop` | Better top | `htop` |
| `df` | Disk usage | `df -h` |
| `du` | Directory size | `du -sh *` |
| `free` | Memory info | `free -h` |
| `uname` | System info | `uname -a` |

## Network

| Command | Description | Example |
|---------|-------------|---------|
| `ping` | Test connectivity | `ping google.com` |
| `curl` | Download | `curl -O url` |
| `wget` | Download | `wget url` |
| `ssh` | Remote login | `ssh user@host` |
| `scp` | Secure copy | `scp file user@host:` |

## Permissions

| Command | Description | Example |
|---------|-------------|---------|
| `chmod` | Change mode | `chmod 755 file` |
| `chown` | Change owner | `chown user:group file` |
| `sudo` | Run as root | `sudo apt update` |

## Process Management

| Command | Description | Example |
|---------|-------------|---------|
| `ps` | Process list | `ps aux` |
| `kill` | Kill process | `kill -9 pid` |
| `jobs` | Background jobs | `jobs` |
| `bg` | Background | `bg %1` |
| `fg` | Foreground | `fg %1` |

## Archives

| Command | Description | Example |
|---------|-------------|---------|
| `tar -czf` | Create archive | `tar -czf out.tar.gz dir/` |
| `tar -xzf` | Extract archive | `tar -xzf in.tar.gz` |
| `zip` | Create zip | `zip archive.zip files` |
| `unzip` | Extract zip | `unzip archive.zip` |

## Useful Flags

### ls
- `-l` Detailed list
- `-a` Show hidden
- `-h` Human sizes
- `-t` Sort by time

### grep
- `-i` Ignore case
- `-r` Recursive
- `-n` Line numbers
- `-v` Invert match

### find
- `-name` Search by name
- `-type f/d` File or directory
- `-mtime` Modified time
- `-exec` Run command