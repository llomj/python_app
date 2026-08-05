# Git Command Reference

## Basic Operations

| Command | Description | Example |
|---------|-------------|---------|
| `git init` | Initialize repo | `git init` |
| `git clone` | Clone repository | `git clone url` |
| `git status` | Show status | `git status` |
| `git add` | Stage changes | `git add .` |
| `git commit` | Save changes | `git commit -m "message"` |
| `git push` | Upload to remote | `git push origin main` |
| `git pull` | Download updates | `git pull origin main` |

## Branching

| Command | Description | Example |
|---------|-------------|---------|
| `git branch` | List branches | `git branch` |
| `git branch <name>` | Create branch | `git branch feature-x` |
| `git checkout` | Switch branch | `git checkout main` |
| `git checkout -b` | Create & switch | `git checkout -b new-branch` |
| `git merge` | Merge branch | `git merge feature-x` |
| `git branch -d` | Delete branch | `git branch -d feature-x` |

## Viewing History

| Command | Description | Example |
|---------|-------------|---------|
| `git log` | Commit history | `git log --oneline` |
| `git diff` | Show changes | `git diff` |
| `git show` | Show commit | `git show commit_id` |
| `git blame` | Who changed what | `git blame file.txt` |

## Remote Operations

| Command | Description |
|---------|-------------|
| `git remote -v` | Show remotes |
| `git remote add` | Add remote |
| `git fetch` | Download changes |
| `git push -u` | Push and track |

## Stashing

| Command | Description |
|---------|-------------|
| `git stash` | Save changes |
| `git stash list` | List stashes |
| `git stash pop` | Apply & remove |
| `git stash drop` | Delete stash |

## ⚠️ Dangerous Commands

- `git reset --hard` - ⚠️ Loses uncommitted changes!
- `git push --force` - ⚠️ Can overwrite remote!
- `git rebase -i` - ⚠️ Rewrites history!
- `git clean -fd` - ⚠️ Deletes untracked files!

## Safe Alternatives

| Instead of | Use |
|------------|-----|
| `git reset --hard` | `git reset --soft HEAD~1` |
| `git push --force` | `git push --force-with-lease` |
| `git rebase` | `git merge` (safer) |

## Common Workflows

### Feature Branch
```bash
git checkout main
git pull
git checkout -b feature/my-feature
# work...
git add .
git commit -m "Add feature"
git push -u origin feature/my-feature
```

### Fix Bug
```bash
git checkout -b bugfix/issue-123
# fix...
git commit -m "Fix bug"
git push
# Create PR
```

## Useful Flags

| Flag | Purpose |
|------|---------|
| `-m` | Commit message |
| `-a` | Auto-stage modified |
| `-v` | Verbose |
| `--amend` | Modify last commit |
| `--force` | Force push |

## Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
git config --global init.defaultBranch main
```