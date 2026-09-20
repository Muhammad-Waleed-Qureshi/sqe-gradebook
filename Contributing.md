# Contributing

## Branching Strategy

This project uses a feature-branch workflow with a single long-lived
`main` branch that must always remain releasable.

New work is done on short-lived branches named by purpose:
- `feature/<slug>` for new features (e.g., `feature/add-student`)
- `fix/<slug>` for bug fixes (e.g., `fix/negative-scores`)
- `docs/<slug>` for documentation-only changes

Commits follow the **Conventional Commits** format
(`<type>(<scope>): <description>`), where `<type>` is one of
`feat`, `fix`, `docs`, `test`, `refactor`, or `chore`.

Every change is submitted via a **pull request** that references its
tracking issue using `Fixes #<n>`. All changes require review and must
pass automated tests before merging. Merges into `main` are done with
**squash merge only** to keep history linear and readable.
