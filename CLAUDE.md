# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Capstone KBS (Knowledge-Based Systems) demo repository demonstrating GitHub best practices with a Python project. The repository emphasizes team collaboration workflows using Pull Requests, CI/CD, and code review processes. The main application (main.py) is a simple demo with full test coverage to showcase proper development practices.

## Development Commands

### Dependency Management
- Install dependencies: `uv sync`
- Run commands through uv: `uv run <command>`

### Running the Application
- Run the demo: `uv run python main.py`

### Code Quality Checks
- Lint code: `uv run ruff check .`
- Format code: `uv run ruff format .`
- Format check (CI): `uv run ruff format --check .`
- Type checking: `uv run pyright` or `uv run mypy`

### Testing
- Run tests: `uv run pytest`
- Run tests quietly (CI): `uv run pytest -q`

## Branch and PR Workflow

### Critical Rules
1. **Never push directly to `main`** - all changes go through PRs
2. **Branch naming conventions:**
   - `feature/` for new features (e.g., `feature/bm25-retrieval`)
   - `fix/` for bug fixes (e.g., `fix/null-input-crash`)
   - `docs/` for documentation (e.g., `docs/readme-update`)
3. **PRs must be:**
   - Small and focused (guideline: <400 lines changed)
   - Reviewed by at least one teammate before merging (or self-review if configured - see `GITHUB_SETTINGS.md`)
   - Have passing CI checks before merging
   - Include clear test instructions in the PR description

### PR Template Structure
Use the template in `pull_request_template.md`:
- **Summary**: What the PR changes (bulleted list)
- **How to Test**: Specific commands or steps (e.g., `pytest`, manual steps)
- **Notes**: Context for reviewers
- **Related**: Optional links to issues/milestones

### Code Review Checklist
When reviewing PRs, verify (from `CODE_REVIEW_CHECKLIST.md`):
- PR title/description clearly explains the change
- PR is small and focused (not a grab-bag)
- Tests added/updated if behavior changed
- CI checks pass
- Handles edge cases, no obvious bugs
- No hard-coded secrets/tokens/credentials
- Code is readable with appropriate comments
- Files placed in appropriate folders

## CI/CD Pipeline

### GitHub Actions Workflows
1. **CI Workflow** (`.github/workflows/ci.yml`):
   - Triggers on PRs and pushes to `main`
   - Runs: uv sync → ruff check → ruff format --check → pytest
   - Uses Python 3.11 on Ubuntu

2. **Auto-assign** (`.github/workflows/auto-assign.yml`):
   - Auto-assigns issues/PRs to @cbrew

### CI Must Pass
All PRs require passing CI checks before merge. The CI ensures:
- Dependencies install correctly
- Code passes linting (ruff)
- Formatting is consistent
- Tests pass

## Architecture Notes

This is a minimal demo Python repository with the following structure:
- `main.py` - Simple demo application with type hints and docstrings
- `tests/` - Test suite with full coverage of main.py functions
- `pyproject.toml` - Project configuration, dependencies, and tool settings
- Policy documents (`pr_policy.md`, `CODE_REVIEW_CHECKLIST.md`, `pull_request_template.md`) define team workflow
- GitHub Actions automate quality checks and issue management

The project follows "uv-first" dependency management - no sys.path manipulations or dynamic imports. All Python tooling (ruff, pytest, pyright, mypy) should be run through `uv run`.

### Code Organization
- All application code should include type hints
- Functions should have descriptive docstrings
- Tests should be organized in the `tests/` directory
- Follow pytest conventions for test naming (test_*.py, test_* functions)