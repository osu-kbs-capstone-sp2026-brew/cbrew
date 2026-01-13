# Code Review Checklist (Capstone KBS)

Use this checklist when reviewing a teammate’s PR.

## ✅ High-level
- [ ] PR title and description clearly explain the change
- [ ] PR is small/focused (not a grab-bag of unrelated edits)
- [ ] Change matches the team’s architecture direction

## 🧪 Testing & reliability
- [ ] PR includes clear “How to test” instructions
- [ ] Tests added or updated if behavior changed
- [ ] CI checks pass (GitHub Actions)

## 🔍 Correctness
- [ ] Handles empty/edge cases reasonably
- [ ] No obvious bugs (exceptions, missing imports, broken paths)
- [ ] No hard-coded secrets, tokens, or credentials

## 🧹 Maintainability
- [ ] Code is readable (names, structure, comments where needed)
- [ ] New files are placed in appropriate folders
- [ ] README/docs updated if needed

## 💬 Review tone
- [ ] Comments are constructive and specific
- [ ] Suggest improvements with “how” not just “what’s wrong”
