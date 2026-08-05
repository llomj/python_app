# Terminal Navigation Guide

## Basic Navigation

### Current Location
```bash
pwd           # Print working directory
```

### List Files
```bash
ls            # Basic list
ls -l         # Detailed list
ls -a         # Include hidden
ls -la        # All + detailed
ls -lh        # Human readable sizes
ls -S         # Sort by size
ls -t         # Sort by time
ls -R         # Recursive
```

### Change Directory
```bash
cd /path      # Absolute path
cd ..         # Parent directory
cd ~          # Home directory
cd -          # Previous directory
cd            # Home (same as ~)
```

## Advanced Navigation

### Directory Stack
```bash
pushd /path   # Change and push to stack
popd          # Pop from stack
dirs          # Show stack
```

### Quick Navigation
```bash
cd -N         # Go to Nth directory in stack
```

## Finding Files

### find
```bash
find . -name "*.txt"
find /home -type f -mtime -7
find . -type d -empty
```

### locate (requires updatedb)
```bash
locate filename
```

### tree (visual)
```bash
tree -L 2        # 2 levels deep
tree -d          # Directories only
tree -a          # Include hidden
```

## Path Types

### Absolute
```
/home/user/project/src
```

### Relative
```
./src
../parent
../../grandparent
```

### Shortcuts
```
~         Home directory
~username  Specific user home
.          Current directory
..         Parent directory
```

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+A` | Beginning of line |
| `Ctrl+E` | End of line |
| `Ctrl+U` | Clear line |
| `Ctrl+L` | Clear screen |
| `Tab`    | Autocomplete |
| `Ctrl+C` | Cancel |
| `Ctrl+Z` | Suspend |

## Terminal Folder Navigation

When working in `/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/AI/termimal`:

```bash
# Subdirectories
cd linux/
cd powershell/
cd docker/
cd security/
cd automation/
cd python/
cd notes/
cd logs/

# Common operations
ls -la
tree -L 2
find . -name "*.md"