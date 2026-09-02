# Test Plan: GradeBook Module

## 1. Introduction
This test plan outlines the testing strategy, scope, schedule, and resources for the GradeBook Python module. The goal is to verify that student records, score tracking, statistical calculations, and data validations meet all functional requirements.

## 2. Test Items
* `src/gradebook/gradebook.py` (`Student` class, score management, and average calculations).

## 3. Features to be Tested
* Adding valid, negative, and non-numeric scores.
* Computing averages (normal, empty list, single score).
* Preventing duplicate roll numbers.
* Case-insensitive name searching (`find_student`).
* Score boundary checks (0 and 100).
* Letter-grade conversions.

## 4. Features Not to be Tested
* **User Interface (UI):** Out of scope because GradeBook is designed as an underlying backend library/module, not a user-facing GUI application.

## 5. Approach
* Manual execution of 12 planned test cases covering functional, boundary, and error-path scenarios. Deficiencies will be tracked via GitHub Issues.

## 6. Item Pass/Fail Criteria
* 100% of planned test cases must be executed.
* Zero Critical or High (P1) defects may remain open for release approval.

## 7. Test Deliverables
* `docs/test-plan.md`
* `docs/test-cases.md`
* `docs/rtm.md`
* `docs/triage-log.md`
* GitHub Issue logs and PR records.

## 8. Environmental Needs
* Python 3.10+ execution environment locally in VS Code.

## 9. Schedule
* Execution and triage performed during the Lab 4 sprint cycle.

## 10. Risks and Mitigation
* **Risk:** Missing core implementation methods causing test blocks. 
* **Mitigation:** Documenting defects immediately via GitHub Issues and prioritizing critical paths.
