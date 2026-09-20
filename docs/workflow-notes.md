# Development Workflow Notes

## Workflow

```text
Idea
  ↓
Issue
  ↓
Branch
  ↓
Pull Request (PR)
  ↓
Review
  ↓
Merge
  ↓
CI
  ↓
Release
```

## QA Engineer Intervention

1. **Idea → Issue:** QA helps clarify the requirement and identifies acceptance criteria, risks, and possible quality concerns.

2. **Issue → Branch:** QA reviews the issue to make sure it is clear, testable, and has enough information for development.

3. **Branch → Pull Request:** QA can review the changes and check whether the implementation matches the requirements.

4. **Pull Request → Review:** QA participates in review by identifying defects, missing tests, and quality issues.

5. **Review → Merge:** QA confirms that required tests and quality checks have been completed before the change is merged.

6. **Merge → CI:** QA monitors automated tests and checks the CI results for failures or regressions.

7. **CI → Release:** QA verifies that the build is stable and that the required quality checks have passed before release.

## Summary

QA can be involved throughout the entire workflow, from clarifying requirements to verifying the final release. Early QA involvement helps identify defects and quality risks before they become more expensive to fix.




---

## Merge Conflict Resolution

During Lab 2 (Task 3), a deliberate merge conflict was created to practice
safe resolution. Two branches — `fix/duplicate-roll-numbers` and
`fix/duplicate-roll-numbers-issue5` — both modified the same region of
`src/gradebook/gradebook.py` to prevent duplicate roll numbers in
`GradeBook.add_student()`.

The first branch was merged into `main`. When the second branch was rebased
against the updated `main`, Git reported a conflict in the `add_student()`
method. The conflict was resolved locally:

1. `git checkout fix/duplicate-roll-numbers-issue5`
2. `git merge main` — Git marked the conflicting hunk in `gradebook.py`
3. The conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) were inspected
4. The correct implementation (identical logic, cleaner formatting) was
   kept and the markers removed
5. `git add src/gradebook/gradebook.py`
6. `git commit -m "fix: resolve merge conflict on add_student duplicate check"`
7. `git push`

The resolved branch was then merged into `main` via PR. After the merge,
`git log --graph --oneline` showed a clean, linear history with the conflict
resolution visible as a normal merge commit.

**Lesson learned:** Both branches touched the same logical area (the
duplicate-roll-number check). Short-lived branches and merging `main` into
the feature branch frequently reduces the size of conflicts when they do
occur.
