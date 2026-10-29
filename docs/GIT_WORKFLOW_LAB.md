# Git Version Control Lab — Week 7

This lab practices Git fundamentals and intermediate workflows using the Task Tracker project. Run commands from the repository root. Replace `YOUR-USERNAME` with your GitHub username.

## 1. Inspect and initialize

```bash
git --version
git status
git log --oneline --decorate --all
```

If this is a new local folder and is not already a repository:

```bash
git init
git branch -M main
git add .
git commit -m "chore: add task tracker starter project"
```

If the folder already has `.git`, do not initialize again or overwrite its history.

## 2. Connect and push to GitHub

Create an **empty** repository on GitHub named `git-version-control-phase3` (do not initialize it with a README if you already have this local commit), then run:

```bash
git remote -v
git remote add origin https://github.com/YOUR-USERNAME/git-version-control-phase3.git
git push -u origin main
```

If `origin` already exists, inspect it with `git remote -v`; do not add a second `origin` or replace it blindly.

## 3. Feature branch → Pull Request → merge (mini project)

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/task-priority
```

Implement a small enhancement (for example, add a priority field to tasks), then test and commit:

```bash
python -m unittest discover -s tests -v
git add .
git commit -m "feat: add task priority"
git push -u origin feature/task-priority
```

On GitHub, open a Pull Request from `feature/task-priority` into `main`. Explain the change, list tests, review the diff, and merge the PR using the repository's merge button. Then sync locally:

```bash
git switch main
git pull --ff-only origin main
git branch -d feature/task-priority
```

Do not delete a branch until its work is safely merged.

## 4. Branch creation and switching

```bash
git branch
git switch -c feature/readme-improvements
# make a change
git add README.md
git commit -m "docs: improve project instructions"
git switch main
git switch feature/readme-improvements
```

Older equivalent for creating and switching: `git checkout -b feature/readme-improvements`.

## 5. Fast-forward vs three-way merge

Fast-forward practice:

```bash
git switch main
git switch -c feature/fast-forward-demo
echo "Fast-forward demo" >> workflow-notes.txt
git add workflow-notes.txt
git commit -m "docs: add fast-forward note"
git switch main
git merge --ff-only feature/fast-forward-demo
```

Three-way merge practice (make changes on both branches before merging):

```bash
git switch -c feature/three-way-demo
echo "Feature branch line" >> workflow-notes.txt
git add workflow-notes.txt && git commit -m "docs: add feature line"
git switch main
echo "Main branch line" >> workflow-notes.txt
git add workflow-notes.txt && git commit -m "docs: add main line"
git merge --no-ff feature/three-way-demo
```

Use a disposable practice branch/repository for exercises that change history.

## 6. Resolve a merge conflict manually

In a disposable practice repository, create two branches that edit the same line differently. Merge one into the other. Git marks the conflict using `<<<<<<<`, `=======`, and `>>>>>>>`.

1. Open the conflicted file and choose/combine the desired content.
2. Remove all conflict markers.
3. Run tests.
4. Stage and commit the resolution:

```bash
git status
git add path/to/conflicted-file
git commit -m "fix: resolve merge conflict"
```

Abort a merge before resolving, if needed: `git merge --abort`.

## 7. Stash, apply, and pop

```bash
git switch -c feature/stash-demo
# edit a tracked file, but do not commit
git stash push -m "work in progress"
git stash list
git stash apply stash@{0}   # restores changes but keeps stash
git stash pop               # restores and removes stash if successful
```

Use `git stash -u` to include untracked files. Check `git status` after applying; stash application can conflict.

## 8. Rebase vs merge

- **Merge** preserves branch history and may create a merge commit; it is usually safer for shared branches.
- **Rebase** replays commits on a new base and creates new commit IDs; it creates a linear history but rewrites commits.
- Avoid rebasing commits that other people have already based work on.

Practice on a private feature branch:

```bash
git switch feature/readme-improvements
git fetch origin
git rebase origin/main
# fix conflicts if prompted, then:
git add path/to/resolved-file
git rebase --continue
# to stop and return to the pre-rebase state:
git rebase --abort
```

## 9. Interactive rebase: squash, fixup, reorder

Only use on commits that have not been shared, unless the team explicitly coordinates history rewriting:

```bash
git switch feature/readme-improvements
git rebase -i HEAD~3
```

In the editor:
- `pick` keeps a commit.
- `reword` changes its message.
- `squash` combines a commit with the previous commit and lets you edit the combined message.
- `fixup` combines it with the previous commit and discards the later message.
- Reorder lines to reorder commits.

Save and close the editor. Resolve conflicts if prompted. Use `git rebase --abort` to cancel.

## 10. Cherry-pick a specific commit

```bash
git log --oneline
git switch -c hotfix/selected-change
git cherry-pick <commit-hash>
```

If conflicts occur, resolve and stage files, then run `git cherry-pick --continue`; cancel with `git cherry-pick --abort`.

## 11. Final checks

```bash
git status
git log --oneline --graph --decorate --all
python -m unittest discover -s tests -v
```

For a useful PR, include a summary, reason for the change, test results, and screenshots/output if applicable.
