# GitHub Pull Request (PR) Policy — Capstone KBS

## Why we use Pull Requests
In this capstone, we will use GitHub Pull Requests (PRs) for essentially all development work. PRs help us:

- coordinate teamwork (avoid overwriting each other)
- keep `main` stable and demo-ready
- make progress visible and trackable
- practice an industry-standard workflow

PRs are not meant to slow you down — they’re here to make your project run reliably.

---

## The Rules (Required)

### 1) No direct pushes to `main`
`main` is protected. **All changes must go through PRs.**

### 2) Work on branches
Create a branch for each unit of work, e.g.
- `feature/bm25-retrieval`
- `fix/null-input-crash`
- `docs/readme-update`

### 3) PRs should be small and focused
A PR should do **one coherent thing**.

Guideline: if your PR is more than ~400 lines changed, it should likely be split.

### 4) Every PR needs a reviewer
Before merging, each PR must be reviewed by **at least one teammate**.

### 5) Every PR must be testable
Each PR must include instructions for how to test it, e.g.
- `pytest`
- `make test`
- a short demo script / manual validation steps

### 6) CI must pass (GitHub Actions)
If your repo has CI checks, they must pass before merging.

---

## Expected Workflow
1. Create a branch
2. Commit changes with clear messages
3. Open a PR early
4. Request review
5. Merge after approval + checks

---



---

## CI (Continuous Integration): what it is and why we use it
CI means that every Pull Request automatically runs a small set of checks (via **GitHub Actions**) such as:

- install the project
- run formatting/lint checks (e.g. **ruff**)
- run tests (e.g. `pytest`)

This prevents “works on my machine” problems and keeps `main` in a demo-ready state.

### Our tooling
- **uv**: fast Python package/project manager (dependency install + running commands)
- **ruff**: fast linter/formatter (catches common bugs and enforces consistent style)

### Setting up CI in a new repo (Python example)
In your repo, create:

- `.github/workflows/ci.yml`

A minimal CI job should:
1. check out code
2. install Python
3. install dependencies using `uv`
4. run `ruff` and tests

(We will provide a starter `ci.yml` file you can copy.)


## What I’m Looking For When I Review PRs
- clear PR goal and description
- a working demo/test path
- changes that don’t break `main`
- good teamwork habits

---

Later in the semester we will introduce additional KBS requirements (representation, traceability, evaluation), and PRs will be the main way you show progress on those.
