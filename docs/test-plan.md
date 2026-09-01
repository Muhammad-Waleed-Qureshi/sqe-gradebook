# Software Test Plan: GradeBook Module

## 1. Introduction
This test plan outlines the testing strategy, scope, resources, and schedule for the **GradeBook** Python application. The goal is to verify that student records, score tracking, validation rules, and statistical calculations function correctly and reliably.

## 2. Test Items
* **Source Code:** `src/gradebook/gradebook.py`
* **Test Scripts / Framework:** Manual test execution suite and future automated unit tests.

## 3. Features to be Tested
* Student profile creation (`name`, `roll_no`, initial scores).
* Score management (`add_score` with valid numbers, positive/negative validation, boundaries).
* Statistical calculations (`average()` for scores, empty lists, single items).
* Record uniqueness (preventing duplicate roll numbers).
* Grade-letter conversions and boundary evaluations.

## 4. Features Not to be Tested (Exclusions)
* **Graphical User Interface (GUI) / Web Frontend:** Out of scope, as GradeBook is currently a core logic Python library module without a web or desktop graphical interface.
* **Database Performance / Scaling:** Out of scope for this version as data is managed in-memory.

## 5. Test Approach
Testing will be conducted via black-box and white-box functional testing, boundary value analysis, and error-guessing. Tests will be executed manually using Python's interactive shell or test scripts, mapping back to explicit requirements in the Requirements Traceability Matrix (RTM).

## 6. Pass/Fail Criteria
* **Pass Criteria:** 95% or more of planned test cases in the execution pass must yield a `Pass` result. All critical functionality (such as score validation and crash prevention on empty lists) must work perfectly.
* **Fail Criteria / Exit Gate:** Testing fails if any `Critical` or `High` severity bug remains open in the issue tracker.

## 7. Test Deliverables
* `docs/test-plan.md` (This document)
* `docs/test-cases.md` (Detailed test cases table)
* `docs/rtm.md` (Requirements Traceability Matrix)
* Execution logs and linked defect issues on GitHub.

## 8. Risks and Contingencies
* **Risk:** Boundary errors or floating-point precision issues in average calculations.
* **Mitigation:** Include explicit boundary value test cases (e.g., scores at exactly 0 and 100) during execution.
