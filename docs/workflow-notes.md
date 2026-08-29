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
