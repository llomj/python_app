# PowerShell Command Reference

## File Operations

| Command | Description | Example |
|---------|-------------|---------|
| `Get-ChildItem` | List files (like ls) | `Get-ChildItem -Path C:\` |
| `Copy-Item` | Copy files | `Copy-Item -Path file.txt -Destination backup.txt` |
| `Move-Item` | Move/rename | `Move-Item -Path old.txt -Destination new.txt` |
| `Remove-Item` | Delete (⚠️ with caution) | `Remove-Item -Path file.txt` |
| `New-Item` | Create file/directory | `New-Item -Path folder -ItemType Directory` |

## System Information

| Command | Description | Example |
|---------|-------------|---------|
| `Get-Process` | List processes | `Get-Process \| Select-Object -First 10` |
| `Get-Service` | List services | `Get-Service \| Where-Object Status -eq Running` |
| `Get-EventLog` | View event logs | `Get-EventLog -LogName System -Newest 10` |
| `Get-ComputerInfo` | System info | `Get-ComputerInfo \| Select-Object OsName` |

## Network

| Command | Description | Example |
|---------|-------------|---------|
| `Test-Connection` | Ping | `Test-Connection google.com` |
| `Invoke-WebRequest` | HTTP requests | `Invoke-WebRequest -Uri https://example.com` |
| `Get-NetIPAddress` | IP config | `Get-NetIPAddress` |

## Process Management

| Command | Description | Example |
|---------|-------------|---------|
| `Start-Process` | Start application | `Start-Process notepad.exe` |
| `Stop-Process` | Kill process | `Stop-Process -Name notepad` |
| `Get-WmiObject` | System info | `Get-WmiObject Win32_Processor` |

## Useful Aliases

| Alias | Full Command |
|-------|--------------|
| `ls` | Get-ChildItem |
| `cd` | Set-Location |
| `cat` | Get-Content |
| `cp` | Copy-Item |
| `mv` | Move-Item |
| `rm` | Remove-Item |
| `grep` | Select-String |

## Common Flags

| Flag | Purpose |
|------|---------|
| `-Recurse` | Include subdirectories |
| `-Force` | Force operation |
| `-Verbose` | Show detailed output |
| `-WhatIf` | Preview (dry-run) |
| `-Confirm` | Ask for confirmation |

## ⚠️ Destructive Commands

- `Remove-Item -Recurse -Force` - Deletes without confirmation
- `Clear-Content` - Clears file contents
- `Stop-Computer` - Shuts down system
- `Restart-Computer` - Reboots system

Always use `-WhatIf` flag first to preview!

## Scripting Basics

```powershell
# Variables
$name = "value"

# If statement
if ($condition) {
    # code
}

# Loop
foreach ($item in $collection) {
    # code
}

# Functions
function My-Function {
    param($param)
    # code
}
```

## Module Management

```powershell
# List modules
Get-Module -ListAvailable

# Import module
Import-Module Az

# Find commands
Get-Command -Module Az
```