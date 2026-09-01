# Software Test Plan: GradeBook Module

## 1. Introduction
This test plan defines the overall testing strategy, scope, schedule, and resources for the GradeBook Python module. The primary objective is to verify that student record management, score validation, and statistical computations comply with all functional specifications.

## 2. Test Items
* Source code modules: `src/gradebook/gradebook.py`
* Test scripts and manual execution sheets located in the `tests/` and `docs/` directories.

## 3. Features to be Tested
* Student profile initialization (`name`, `roll_no`, and score attributes).
* Score management (`add_score()` with valid numbers, positive/negative validation, and boundary checks).
* Statistical processing (`average()` calculation for scores, handling single elements and empty lists).
* Data integrity rules (preventing duplicate roll numbers).
* Grade-letter mapping and boundary logic.

## 4. Features Not to be Tested (Exclusions)
* **Graphical User Interface (GUI) / Web Interface:** Out of scope. GradeBook is strictly designed as a core logic Python library module rather than a standalone desktop or web application, meaning no UI components require visual verification.
* **Database Persistence Layer:** Out of scope for this phase since student records are currently managed through in-memory data structures.

## 5. Test Approach
Testing will utilize a combination of black-box functional testing, boundary value analysis, and error-guessing. Test cases will be executed manually against the codebase, mapped directly through the Requirements Traceability Matrix (`docs/rtm.md`), and tracked using GitHub Issues for any failures.

## 6. Pass/Fail Criteria
* **Pass Criteria:** At least **95%** of the planned test cases in the execution suite must yield a `Pass` result, and zero **Critical** or **High** severity defects may remain open in the issue tracker.
* **Fail Criteria:** Testing is deemed a failure if core validation checks fail or if any critical runtime crash occurs during normal usage paths.

## 7. Test Deliverables
* Test Plan document (`docs/test-plan.md`)
* Detailed Test Cases table (`docs/test-cases.md`)
* Requirements Traceability Matrix (`docs/rtm.md`)
* Bug reports and automated/manual execution logs on GitHub.

## 8. Environmental Needs
* Python 3.10+ runtime environment installed locally or within the development container.
* VS Code code editor with Git integration.
* GitHub platform access for issue tracking, project boards, and pull requests.

## 9. Schedule
* **Test Plan & Test Case Authoring:** Day 1
* **Manual Execution Pass:** Day 2
* **Defect Filing and Regression Verification:** Day 3

## 10. Risks and Contingencies
* **Risk:** Floating-point rounding discrepancies during statistical average calculations.
* **Mitigation:** Incorporate strict boundary value test cases to verify decimal precision output.
