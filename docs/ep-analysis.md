# Equivalence Partitioning Analysis — Lab 5

## 1. Input: `letter_grade(score)`

**Rule:** A numeric score is mapped to a letter grade. Valid range is 0–100.

| Class | Range | Type | Representative | Expected Result |
|---|---|---|---|---|
| Invalid-low | score < 0 | Invalid | -10 | ValueError |
| F | 0 – 59 | Valid | 45 | "F" |
| D | 60 – 69 | Valid | 65 | "D" |
| C | 70 – 79 | Valid | 75 | "C" |
| B | 80 – 89 | Valid | 85 | "B" |
| A | 90 – 100 | Valid | 95 | "A" |
| Invalid-high | score > 100 | Invalid | 150 | ValueError |

**Test file:** `tests/test_letter_grade.py`

---

## 2. Input: number of scores per student (`Roster.add_student`)

**Rule:** A student must have between 1 and 6 scores when added to the roster.

| Class | Range | Type | Representative | Expected Result |
|---|---|---|---|---|
| Invalid-low | 0 scores | Invalid | 0 | ValueError |
| Valid | 1 – 6 scores | Valid | 3 | Accepted |
| Invalid-high | 7+ scores | Invalid | 8 | ValueError |

**Test file:** `tests/test_roster.py`

---

## 3. Input: student name (`validate_name`)

**Rule:** Non-empty string, max 50 characters, letters/spaces/hyphens only.

| Class | Rule | Type | Representative | Expected Result |
|---|---|---|---|---|
| Valid typical | Letters + space | Valid | "Ali Khan" | Accepted |
| Empty string | length 0 | Invalid | "" | ValueError |
| Over-length | length > 50 | Invalid | "A" * 51 | ValueError |
| Illegal digits | contains digits | Invalid | "Ali123" | ValueError |
| Illegal symbols | contains symbol | Invalid | "Ali@Khan" | ValueError |

**Test file:** `tests/test_validate_name.py`

---

## 4. EP Limitation Note

Equivalence Partitioning tests **one representative value per class**. This is efficient, but it has a blind spot: **boundary values are not tested**. For example, testing score `85` proves class `B` works, but does **not** catch off-by-one bugs at `89` vs `90` or `59` vs `60`.

This gap is closed in **Lab 6 (Boundary Value Analysis)**, where we explicitly test min-1, min, min+1, max-1, max, max+1 for each boundary.

---

## 5. Test Execution Summary

All EP tests pass:
tests/test_letter_grade.py::test_letter_grade_valid_classes[45-F] PASSED
tests/test_letter_grade.py::test_letter_grade_valid_classes[65-D] PASSED
tests/test_letter_grade.py::test_letter_grade_valid_classes[75-C] PASSED
tests/test_letter_grade.py::test_letter_grade_valid_classes[85-B] PASSED
tests/test_letter_grade.py::test_letter_grade_valid_classes[95-A] PASSED
tests/test_letter_grade.py::test_letter_grade_invalid_classes[-10] PASSED
tests/test_letter_grade.py::test_letter_grade_invalid_classes[150] PASSED

tests/test_roster.py::test_roster_score_count_classes[0-False] PASSED
tests/test_roster.py::test_roster_score_count_classes[3-True] PASSED
tests/test_roster.py::test_roster_score_count_classes[8-False] PASSED

tests/test_validate_name.py::test_valid_typical_name PASSED
tests/test_validate_name.py::test_invalid_names[] PASSED
tests/test_validate_name.py::test_invalid_names[A*51] PASSED
tests/test_validate_name.py::test_invalid_names[Ali123] PASSED
tests/test_validate_name.py::test_invalid_names[Ali@Khan] PASSED

==================== 15 passed in 0.12s ====================

text

**Total: 15 test cases, all passing.**
