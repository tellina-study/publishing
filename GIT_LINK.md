# Git link (harness-control#306)

This folder is linked to `tellina-study/publishing` via the configured git connection `study_token` (https://github.com/tellina-study/publishing.git).

Auth method: `token` (stored token).

`git pull`/`git fetch`/`git push` run in this session's own shell are already authenticated -- the credential is set up in this session's environment, not stored in this repo's `.git/config`. You do not need to ask for, enter, or store a credential yourself. The `gh` CLI (e.g. `gh pr create`, `gh issue view`) is authenticated the same way, with the same credential -- no separate `gh auth login` needed either.

This directory is a git worktree of the folder's clone, checked out on its own branch `hc/sdlc-83361639`. Getting work OUT: this branch is directly visible from the folder's own shared checkout via the shared `.git` object store, so a local merge there needs no push; pushing the branch and opening a PR is the standard route to review/merge elsewhere. Both are equally valid -- follow your own instructions/workflow.
