# Conventional Commit Message Hook

This is a `pre-commit` hook that enforces [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) in your Git commit messages.

##  Why Use It?

1. Ensures consistency across commits   
2. Makes your project history readable and structured  
3. Works with any programming language

---

##  Installation

### 1. Install `pre-commit` (if not already installed)

```bash
pip install pre-commit
```
### 2. Add this hook to your project
In your project's root, create or update `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/zakachaara/commit-msg-hook
    rev: v1.0.0  # Replace with the latest version/tag
    hooks:
      - id: conventional-commit-msg
```
### 3. Install the hook
```bash
pre-commit install --hook-type commit-msg
```
---
# Required Format for the Message :
Your commit message must follow this pattern:
```xml
<type>(optional-scope): <description>
```
## Examples 
```python
feat(auth): add OAuth2 login support
fix(ui): resolve layout overflow on small screens
docs(readme): update setup instructions
refactor(core): simplify data pipeline
chore: update dependencies
```
## Invalid examples
```bash
"update code"
"final version"
"bug fix"
"temp commit"
```
---
# Supported types : 
| Type       | Purpose                                |
| ---------- | -------------------------------------- |
| `feat`     | A new feature                          |
| `fix`      | A bug fix                              |
| `docs`     | Documentation changes only             |
| `style`    | Code style changes (formatting only)   |
| `refactor` | Code restructuring (no feature change) |
| `perf`     | Performance improvements               |
| `test`     | Adding or updating tests               |
| `chore`    | Maintenance (build, CI, deps)          |

---
## Adding the `BREAKING CHANGE` footer
You can indicate breaking changes with the BREAKING CHANGE footer:

```text
feat(api): change response format

BREAKING CHANGE: /users endpoint now returns data in a new format
```
