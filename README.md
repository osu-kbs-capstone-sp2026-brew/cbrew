# cbrew - Capstone KBS Demo Repository

This repository demonstrates best practices for collaborative software development using GitHub Pull Requests, code review, and continuous integration.

## Overview

This is a Python project showcasing team workflow processes for the Capstone Knowledge-Based Systems course. The repository emphasizes:

- Pull Request-based development workflow
- Mandatory code review before merging
- Automated CI/CD with GitHub Actions
- Code quality enforcement (ruff, pytest, pyright, mypy)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- uv (Python package manager)

### Setup
```bash
# Clone the repository
git clone <repo-url>
cd cbrew

# Install dependencies
uv sync

# Run the demo
uv run python main.py

# Run tests
uv run pytest

# Check code quality
uv run ruff check .
uv run ruff format --check .
uv run pyright
uv run mypy .
```

## Development Workflow

### The Pull Request Process

All changes to the `main` branch must go through Pull Requests. **Direct pushes to `main` are not allowed.**

#### 1. Create a Branch

Use descriptive branch names with prefixes:
- `feature/` for new features (e.g., `feature/add-retrieval`)
- `fix/` for bug fixes (e.g., `fix/null-pointer`)
- `docs/` for documentation (e.g., `docs/update-readme`)

```bash
git checkout -b feature/my-new-feature
```

#### 2. Make Changes and Commit

Follow the small commits philosophy with quality checks:
```bash
# Make your changes
# Run quality checks
uv run ruff check .
uv run ruff format .
uv run pytest

# Commit your changes
git add .
git commit -m "Add feature X"
```

#### 3. Push and Create PR

```bash
git push -u origin feature/my-new-feature
```

Then create a Pull Request on GitHub. The PR template will guide you to include:
- **Summary**: What the PR changes (bullet points)
- **How to Test**: Specific commands or manual steps
- **Notes**: Context for reviewers
- **Related**: Links to issues or milestones (optional)

See `pull_request_template.md` for the full template.

#### 4. Code Review

Every PR requires at least one teammate review before merging. Reviewers should use the checklist in `CODE_REVIEW_CHECKLIST.md`:

**High-level checks:**
- PR title and description clearly explain the change
- PR is small and focused (guideline: <400 lines)
- Change aligns with team architecture

**Testing & reliability:**
- Clear "How to test" instructions
- Tests added/updated for behavior changes
- CI checks pass

**Correctness:**
- Handles edge cases appropriately
- No obvious bugs or missing imports
- No hard-coded secrets or credentials

**Maintainability:**
- Code is readable with clear naming
- Files organized appropriately
- Documentation updated if needed

#### 5. Merge After Approval

Once the PR is approved and all CI checks pass, it can be merged to `main`.

### PR Size Guidelines

Keep PRs small and focused:
- **Guideline**: <400 lines changed
- **Goal**: One coherent change per PR
- **Why**: Smaller PRs are easier to review, test, and merge

If your change is large, break it into multiple PRs with incremental functionality.

## Continuous Integration

GitHub Actions automatically runs checks on every PR:

1. **Dependency Installation**: `uv sync`
2. **Linting**: `uv run ruff check .`
3. **Formatting**: `uv run ruff format --check .`
4. **Tests**: `uv run pytest -q`

All checks must pass before merging. See `.github/workflows/ci.yml` for details.

## Project Policies

### Required Reading

- **`pr_policy.md`**: Complete PR workflow requirements and rationale
- **`CODE_REVIEW_CHECKLIST.md`**: What to check when reviewing PRs
- **`pull_request_template.md`**: Template for PR descriptions

### Key Rules

1. **No direct pushes to `main`** - all changes via PRs
2. **One reviewer minimum** - every PR needs approval
3. **CI must pass** - all automated checks must succeed
4. **Include test instructions** - tell reviewers how to verify changes
5. **Keep PRs small** - easier to review and less risky

## Code Quality Tools

This project uses modern Python tooling:

- **uv**: Fast Python package manager and command runner
- **ruff**: Fast linter and formatter (replaces flake8, black, isort)
- **pytest**: Testing framework
- **pyright**: Type checker (fast, VS Code integration)
- **mypy**: Additional type checking

Configuration is in `pyproject.toml`.

## Repository Structure

```
cbrew/
├── .github/
│   └── workflows/       # GitHub Actions CI/CD
│       ├── ci.yml       # Main CI pipeline
│       ├── auto-assign.yml
│       └── proof-html.yml
├── main.py              # Demo Python application
├── pyproject.toml       # Project configuration and dependencies
├── README.md            # This file
├── pr_policy.md         # Pull Request policy (required reading)
├── CODE_REVIEW_CHECKLIST.md  # Code review guidelines
└── pull_request_template.md  # PR template

```

## Getting Help

- Review the policy documents in this repository
- Ask teammates for clarification
- Check GitHub Actions logs if CI fails

## License

Educational project for Capstone KBS course.
