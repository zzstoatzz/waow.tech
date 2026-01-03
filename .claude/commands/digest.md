---
description: generate a digest of work shipped over the last month
allowed-tools: Bash(git:*), Bash(ls:*), Bash(gh:*), Bash(find:*), Bash(stat:*), Read, Glob, Grep, Task
---

generate a comprehensive digest of what i've shipped over the last month.

## step 1: detect identity

determine who the user is by running these commands:
- `git config user.email` - primary identifier for commit authorship
- `git config user.name` - display name
- `gh api user --jq .login 2>/dev/null` - github username (skip if gh unavailable)

## step 2: detect source directories

check for these directory structures and skip any that don't exist:

**github repos**: `~/github.com/{username}` where username matches the gh login or can be inferred from directory contents

**tangled repos**: `~/tangled.sh/@{handle}` - look for directories matching `@*` pattern

**gitlab repos**: `~/gitlab.com/{username}` (if exists)

for each provider, only proceed if the base directory exists (e.g., `~/github.com`).

## step 3: find recently modified repos

for each detected source directory:
1. list subdirectories and check modification times
2. for repos modified in the last 30 days, run: `git log --oneline --author="<email>" --since="1 month ago" | head -20`
3. skip repos with no commits from this user in the time period

also check for work contributions in common locations:
- employer repos (other directories under ~/github.com that aren't the user's username)
- look for repos where the user has commits but doesn't own the repo

## step 4: gather project metadata

for each active repo, try to determine:
- **what it is**: read README.md first paragraph or pyproject.toml description
- **live url**: check for fly.toml (app name -> {app}.fly.dev), wrangler.toml, vercel.json, or CNAME files
- **package name**: check pyproject.toml `[project] name` for installable packages

## step 5: generate digest

organize the output as markdown:

```
## shipped this month

### projects
| project | description | link |
|---------|-------------|------|
| ... | ... | ... |

### contributions
notable commits to other projects (employer, open source, etc.)

### themes
- common patterns or focus areas this month
```

include valid links wherever possible - deployed URLs, github repos, pypi packages.

format should be suitable for embedding in a personal site or sharing as a status update.
