# PowerShell Troubleshooting Guide

## Common Issues & Solutions

### Script Won't Run

**Symptoms**: "Cannot be loaded because running scripts is disabled"

**Diagnosis**:
```powershell
Get-ExecutionPolicy
```

**Solutions**:
```powershell
# Check current policy
Get-ExecutionPolicy -List

# Allow scripts (for current user)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Or for all (requires admin)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

### Module Not Found

**Symptoms**: "Module 'ModuleName' was not found"

**Diagnosis**:
```powershell
Get-Module -ListAvailable
$env:PSModulePath -split ':'
```

**Solutions**:
```powershell
# Install module
Install-Module -Name ModuleName -Force

# Or from gallery
Install-Package -Name ModuleName -ProviderName PSGallery
```

### Permission Denied

**Diagnosis**:
```powershell
whoami /all
Get-Process -Id $PID | Select-Object -ExpandProperty Principal
```

**Solutions**:
1. Run as Administrator
2. Check UAC settings
3. Use `RunAs`

### Execution Slow

**Diagnosis**:
```powershell
Measure-Command { your-command }
Get-History | Measure-Object
```

**Solutions**:
1. Clear history: `Clear-History`
2. Check profile: `$PROFILE`
3. Disable modules: `Get-Module | Where-Object {$_.ModuleType -eq 'Binary'}`

### Network Issues

**Diagnosis**:
```powershell
Test-NetConnection google.com
Invoke-WebRequest -Uri https://google.com
```

**Solutions**:
1. Check proxy: `$env:HTTP_PROXY`
2. Reset network: `netsh winsock reset`
3. Clear DNS: `Clear-DnsClientCache`

### Service Won't Start

**Diagnosis**:
```powershell
Get-Service -Name ServiceName | Select-Object Status, StartType
Get-WinEvent -LogName System -MaxEvents 10
```

**Solutions**:
```powershell
# Restart service
Restart-Service -Name ServiceName -Force

# Check dependencies
Get-Service -Name ServiceName | Select-Object -ExpandProperty DependentServices
```

### Variable Issues

**Common problems**:
- `$null` vs empty string
- Scope issues
- Type conversion

**Solutions**:
```powershell
# Check if null or empty
if ([string]::IsNullOrEmpty($var)) { }

# Explicit type
[int]$number = "42"

# Force scope
$script:var = "value"
```

## Diagnostic Commands

| Issue | Command |
|-------|---------|
| Errors | `$Error` |
| History | `Get-History` |
| Modules | `Get-Module` |
| Processes | `Get-Process` |
| Services | `Get-Service` |
| Events | `Get-WinEvent -LogName System` |

## Profile Debugging

```powershell
# Check profile path
$PROFILE

# Test profile
. $PROFILE

# Find slow commands
(Get-History).Duration | Sort-Object -Descending | Select-Object -First 5
```

## Common Fixes

```powershell
# Clear cache
Remove-Item $env:TEMP\* -Recurse -Force

# Reset PowerShell
Remove-Item (Join-Path $PSHOME "Profile.ps1")

# Update help
Update-Help
```