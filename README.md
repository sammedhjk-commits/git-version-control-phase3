# Git Version Control — Phase 3

A beginner-friendly, hands-on project for practicing Git fundamentals and intermediate workflows from Week 7. The sample application is a small Python Task Tracker; the main deliverable is the Git workflow lab and the feature-branch → Pull Request → merge simulation.

## Learning objectives

- `git init`, `clone`, `add`, `commit`, `push`, and `pull`
- Create and switch branches with `checkout -b` and `switch`
- Compare fast-forward and three-way merges
- Resolve merge conflicts manually
- Use `git stash`, `stash apply`, and `stash pop`
- Understand Pull Requests and code review
- Compare rebase with merge
- Use interactive rebase to squash, fixup, and reorder commits
- Apply one commit with `git cherry-pick`

## Features

- Small in-memory task tracker with add, list, complete, and remove operations
- Validation for blank task titles and errors for unknown task IDs
- Unit tests using Python's built-in `unittest`
- Step-by-step Git workflow lab with commands and safety notes

## Technology stack

- Python 3.9+
- Git
- Python standard library only; no third-party dependencies

## Project structure

```text
git-version-control-phase3/
├── .gitignore
├── README.md
├── main.py
├── docs/
│   └── GIT_WORKFLOW_LAB.md
├── src/
│   ├── __init__.py
│   └── task_tracker.py
└── tests/
    └── test_task_tracker.py
```

## Setup

Check that Python and Git are installed:

```bash
python --version
git --version
```

Clone your GitHub repository after you upload it:

```bash
git clone https://github.com/YOUR-USERNAME/git-version-control-phase3.git
cd git-version-control-phase3
```

Or open the downloaded project folder directly in VS Code.

## Run the sample application

```bash
python main.py
```

Expected output:

```text
Gitflow Practice — Task Tracker
Add a sample task and show it:
#1: Create a feature branch [open]
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Mini project: feature branch → PR → merge

1. Create a feature branch from `main`.
2. Implement a small, meaningful improvement.
3. Run tests and commit the change.
4. Push the feature branch to GitHub.
5. Open a Pull Request into `main`.
6. Review the diff and test evidence.
7. Merge the PR on GitHub.
8. Pull the updated `main` branch locally and remove the merged local feature branch.

Detailed commands and exercises are in [`docs/GIT_WORKFLOW_LAB.md`](docs/GIT_WORKFLOW_LAB.md).

## GitHub upload

Create a new, empty GitHub repository first. Then, from this project directory, run:

```bash
git init
git branch -M main
git add .
git commit -m "chore: add Git version control lab project"
git remote add origin https://github.com/YOUR-USERNAME/git-version-control-phase3.git
git push -u origin main
```

If Git is already initialized, inspect `git status` and `git remote -v` first. If a remote already exists, verify it rather than blindly adding or replacing it. Do not force-push.

## Notes

- The sample app stores tasks in memory, so tasks reset when the program exits.
- Use a disposable repository or practice branch for conflict and history-rewriting exercises.
- Never commit tokens, passwords, private keys, or `.env` files.
