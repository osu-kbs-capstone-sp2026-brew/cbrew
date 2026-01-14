# GitHub Repository Settings Guide

This guide explains how to configure GitHub branch protection to allow self-review of PRs while maintaining code quality through automated CI checks.

## Branch Protection Rules for `main`

### Recommended Settings for Solo or Small Team Development

To allow self-review while maintaining quality gates:

1. **Go to**: Repository → Settings → Branches → Add branch protection rule

2. **Branch name pattern**: `main`

3. **Protection settings**:

   ✅ **Require a pull request before merging**
   - This ensures all changes go through PRs (no direct pushes)
   - ⚠️ **Do NOT check** "Require approvals" (or set to 0)
   - This allows you to merge your own PRs

   ✅ **Require status checks to pass before merging**
   - Search for and select: `test` (the CI workflow job name)
   - ✅ Check "Require branches to be up to date before merging"
   - This ensures all automated tests pass before merge

   ✅ **Require conversation resolution before merging** (optional)
   - Ensures you address any comments on your PR

   ⚠️ **Do NOT check** "Require review from Code Owners"
   - Only needed if using CODEOWNERS file

   ⚠️ **Do NOT check** "Dismiss stale pull request approvals when new commits are pushed"
   - Not needed for self-review workflow

   ✅ **Include administrators** (optional but recommended)
   - Applies rules even to repo admins for consistency

4. **Click "Create" or "Save changes"**

### What This Configuration Does

**Allows:**
- ✅ Creating and merging your own PRs (self-review)
- ✅ Merging immediately after CI passes
- ✅ Solo development with quality gates

**Requires:**
- ✅ All changes through PRs (no direct pushes to main)
- ✅ All CI checks must pass (ruff, pytest)
- ✅ Branch must be up-to-date with main

**Prevents:**
- ❌ Direct pushes to main
- ❌ Merging with failing tests
- ❌ Merging without running quality checks

## Alternative: Team Collaboration Settings

For teams that want peer review:

1. Follow all settings above, BUT:
   - ✅ Check "Require approvals"
   - Set to `1` or more approvals required

2. Additional recommended settings:
   - ✅ "Dismiss stale pull request approvals when new commits are pushed"
   - ⚠️ Do NOT check "Allow specified actors to bypass required pull requests"

## Verifying Your Settings

After configuration, test by:

1. Create a branch: `git checkout -b test/verify-settings`
2. Make a small change to README.md
3. Push: `git push -u origin test/verify-settings`
4. Create a PR on GitHub
5. Verify:
   - ✅ CI checks run automatically
   - ✅ You can merge after checks pass (if self-review enabled)
   - ❌ You cannot merge before checks pass

## Current CI Checks

The `test` job in `.github/workflows/ci.yml` runs:
1. `uv sync` - Install dependencies
2. `uv run ruff check .` - Lint code
3. `uv run ruff format --check .` - Check formatting
4. `uv run pytest -q` - Run tests

All must pass for the status check to succeed.

## Workflow Examples

### Solo Development (Self-Review Enabled)
```bash
git checkout -b feature/new-feature
# Make changes
uv run ruff check . && uv run ruff format . && uv run pytest
git commit -am "Add new feature"
git push -u origin feature/new-feature
# Create PR on GitHub, wait for CI, then merge
```

### Team Development (Approvals Required)
```bash
git checkout -b feature/new-feature
# Make changes
uv run ruff check . && uv run ruff format . && uv run pytest
git commit -am "Add new feature"
git push -u origin feature/new-feature
# Create PR, request review from teammate, wait for approval + CI, then merge
```

## Additional Resources

- [GitHub Docs: Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [GitHub Docs: Status Checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)
