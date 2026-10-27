# Boundary Value Analysis — Lab 6

Boundary Value Analysis (BVA) tests values at and around the edges of valid input ranges. It helps detect off-by-one defects and incorrect boundary conditions. This document lists the boundaries and expected results for the three functions under test in the GradeBook project.

## 1. `letter_grade(score)` — Score Domain Edges

**Valid score range:** 0–100

**Grade cut-offs:** 60, 70, 80, and 90.

| Boundary | Value - 1 | Value | Value + 1 |
|---|---|---|---|
| Domain minimum (0) | -1 → `ValueError` | 0 → F | 1 → F |
| F/D cut-off (60) | 59 → F | 60 → D | 61 → D |
| D/C cut-off (70) | 69 → D | 70 → C | 71 → C |
| C/B cut-off (80) | 79 → C | 80 → B | 81 → B |
| B/A cut-off (90) | 89 → B | 90 → A | 91 → A |
| Domain maximum (100) | 99 → A | 100 → A | 101 → `ValueError` |

**Total cases:** 18 (6 boundaries × 3 values)

**Test file:** `tests/test_letter_grade_bva.py`

## 2. `Roster.add_student()` — Score-Count Rule

**Valid score count:** 1–6, inclusive.

| Boundary | Value - 1 | Value | Value + 1 |
|---|---|---|---|
| Minimum (1) | 0 → `ValueError` | 1 → Accepted | 2 → Accepted |
| Maximum (6) | 5 → Accepted | 6 → Accepted | 7 → `ValueError` |

**Total cases:** 6

**Test file:** `tests/test_roster.py`

**Test function:** `test_roster_score_count_boundaries`

## 3. `validate_name()` — Name-Length Rule

A valid name must not be empty after trimming whitespace and must contain no more than 50 characters. It must also satisfy the function's character-validation rules.

| Boundary | Input Length | Expected Result |
|---|---:|---|
| Minimum invalid length | 0 | `ValueError` |
| Minimum valid length | 1 | Accepted |
| Just below maximum | 49 | Accepted |
| Maximum valid length | 50 | Accepted |
| Above maximum | 51 | `ValueError` |

The length tests should use valid characters, such as repeated letters, so that they test the length rule rather than unrelated character-validation rules.

**Required boundary cases:** 5

**Test file:** `tests/test_validate_name.py`

**Test function:** `test_validate_name_length_boundaries`

## 4. Defect Found During Testing

During the review of the GradeBook project, a defect was reported in the `Student` class: the `get_grade()` method was missing, preventing a student object from directly obtaining a letter grade based on its stored scores.

According to the recorded project history, this defect was filed as Issue #15 and fixed through PR #17 on the `fix/get-grade-method` branch.

- **Issue:** #15 — Defect: Student object missing `get_grade()` method
- **Pull request:** #17 — `fix(student): add get_grade() method — Fixes #15`
- **Branch:** `fix/get-grade-method`
- **Regression tests:** `tests/test_get_grade.py`, reported to contain 8 test cases
- **Expected outcome:** The method returns the letter grade calculated from the student's average score.
- **Closure:** The issue is automatically closed by the `Fixes #15` keyword when the relevant pull request is merged.

**Verification note:** Confirm the issue, pull request, merge status, and test results in the actual repository. The reported defect was found during a manual coverage review. This alone does not establish that it was discovered specifically through BVA, as required by the Lab 6 submission checklist.

## 5. EP + BVA Combined Test Suite

The following results were recorded for the individual test files:

| Test file | Purpose | Reported result |
|---|---|---:|
| `tests/test_letter_grade.py` | Lab 5 equivalence partitioning (EP) | 7 passed |
| `tests/test_letter_grade_bva.py` | Lab 6 boundary testing | 18 passed |
| `tests/test_roster.py` | EP + BVA | 9 passed |
| `tests/test_validate_name.py` | EP + BVA | 10 passed |
| `tests/test_get_grade.py` | Regression testing | 8 passed |
| **Total** | | **52 passed** |

These figures are the previously recorded results and must be verified with a fresh full-suite run before submission.

Run the following command from the project root:

`pytest -v`

Update this section if the actual results differ.

### Purpose of the Combined Suite

- **Equivalence Partitioning (EP):** Tests representative inputs from valid and invalid groups.
- **Boundary Value Analysis (BVA):** Tests values immediately below, at, and above important boundaries.
- **Regression Testing:** Checks that previously fixed defects do not return.

Together, these techniques improve confidence in score validation, letter-grade assignment, roster score-count validation, name-length validation, and the `Student` class functionality.

## 6. Conclusion

The boundary tables identify the important input limits and expected results for the three functions. The corresponding pytest tests should verify these expectations, detect boundary-related defects, and confirm that fixes do not break existing functionality.

The file is ready for final verification once the test results and the required boundary-discovered defect, GitHub Issue, and merged pull request have been confirmed.