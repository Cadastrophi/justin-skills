# Git worktrees for Junior Dev

## Mental model

A Git branch is a movable name pointing to a commit. A Git worktree is a folder where one branch is checked out.

The primary Vellum folder and a feature worktree share the same underlying Git object database, remotes, and commits, but each has its own checked-out files, staging area, and branch:

```text
vellum/                         primary checkout; leave untouched
vellum-worktrees/add-sharing/   isolated files on codex/add-sharing
```

Edits made in the feature folder do not change the files visible in the primary folder. Commits made in either folder are visible to the shared repository. Git normally prevents the same branch from being checked out in two worktrees simultaneously.

A worktree is not a security or infrastructure sandbox. It may still use shared environment files, credentials, databases, ports, browser cookies, cloud services, and third-party accounts. Inspect those separately before running code.

## Creating a feature worktree

From the primary checkout:

1. Inspect `git status`, `git worktree list`, branches, and remotes without changing them.
2. Fetch `origin` and resolve the exact latest `origin/dev` commit.
3. Choose a unique `codex/<short-slug>` branch and a unique sibling directory outside the primary repository folder.
4. Create the worktree and branch from `origin/dev`.
5. Enter the new folder and verify a clean status, the expected branch, and the expected merge base.

The command shape is:

```bash
git worktree add -b codex/<short-slug> <absolute-sibling-path> origin/dev
```

Resolve and validate every placeholder before running the command. Do not use an existing directory, overwrite another worktree, or reuse a branch already checked out elsewhere.

Record the absolute worktree path, branch name, and base commit in the task handoff.

## What gets merged

You do not merge a worktree. You merge the branch checked out inside it.

The Junior Dev flow is:

```text
feature worktree
    contains codex/<feature> branch
        -> push branch to origin
        -> open draft PR: codex/<feature> -> dev
        -> user and cofounder review
        -> user or cofounder merges the PR
        -> GitHub updates dev
```

The worktree is only a local folder that makes the branch safer to work on. Closing a terminal or removing the folder does not merge code.

Junior Dev must never merge the PR, target `main`, enable auto-merge, or mark the draft ready.

## Concurrent changes on dev

Record the initial `origin/dev` commit. Before the first push, fetch again and compare that commit with the new `origin/dev`.

Review upstream changes for:

- the same files;
- shared schemas or public types;
- database migrations and their ordering;
- dependency or lockfile changes;
- API contracts;
- behavior that changes the assumptions of the feature.

When changes do not overlap, rebase the unpublished branch onto the latest `origin/dev` and rerun affected checks. When they overlap semantically or cause conflicts, stop for user/cofounder coordination. Never resolve by blindly discarding one side.

Do not force-push a published branch without explicit authorization.

## Cleanup after review

Cleanup happens only after the user confirms that the pull request was merged or closed.

1. Identify the exact worktree path and branch with `git worktree list`.
2. Verify the feature worktree has no uncommitted or untracked work.
3. Confirm the PR status and whether its commits need to remain accessible.
4. Ask for authorization to remove the exact worktree and branches.
5. Remove the worktree through Git rather than deleting its directory manually.
6. Prune stale worktree metadata if necessary.
7. Delete the local feature branch only after it is merged or intentionally abandoned.
8. Delete the remote branch only if the user requests it and GitHub has not already done so.

Typical command shapes are:

```bash
git worktree remove <absolute-worktree-path>
git worktree prune
git branch -d codex/<short-slug>
git push origin --delete codex/<short-slug>
```

Treat removal and branch deletion as separate destructive actions. Validate exact targets and obtain authorization; never use force removal or `git branch -D` merely to make cleanup succeed.

After cleanup, the merged code is available by updating the primary checkout's `dev` branch through the repository's normal workflow. The absence of the feature worktree does not remove merged commits.
