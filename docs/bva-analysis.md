# Boundary Value Analysis — Lab 6

Boundary Value Analysis (BVA) tests the edges of each equivalence class
(min-1, min, min+1, max-1, max, max+1) where off-by-one defects most
commonly hide. This document lists boundaries for all three inputs under
test and the expected results.

---

## 1. `letter_grade(score)` — Score Domain Edges

**Cut-offs:** 0, 60, 70, 80, 90, 100

| Boundary | value-1 | value | value+1 | Expected at each |
|---|---|---|---|---|
| Domain min (0) | -1 → ValueError | 0 → "F" | 1 → "F" | ValueError / F / F |
| F/D (60) | 59 → "F" | 60 → "D" | 61 → "D" | F / D / D |
| D/C (70) | 69 → "D" | 70 → "C" | 71 → "C" | D / C / C |
| C/B (80) | 79 → "C" | 80 → "B" | 81 → "B" | C / B / B |
| B/A (90) | 89 → "B" | 90 → "A" | 91 → "A" | B / A / A |
| Domain max (100) | 99 → "A" | 100 → "A" | 101 → ValueError | A / A / ValueError |

**Total cases: 18** (6 rows × 3 values)
**Test file:** `tests/test_letter_grade_bva.py`

---

## 2. `Roster.add_student` — Score-Count Rule (1–6 valid)

**Boundaries:** 0/1 and 6/7

| Boundary | value-1 | value | value+1 | Expected at each |
|---|---|---|---|---|
| Min (1) | 0 → ValueError | 1 → Accepted | 2 → Accepted | ValueError / Accepted / Accepted |
| Max (6) | 5 → Accepted | 6 → Accepted | 7 → ValueError | Accepted / Accepted / ValueError |

**Total cases: 6**
**Test file:** `tests/test_roster.py` (function `test_roster_score_count_boundaries`)

---

## 3. `validate_name` — Length Rule (1–50 valid)

**Boundaries:** 0/1 and 50/51

| Boundary | value-1 | value | value+1 | Expected at each |
|---|---|---|---|---|
| Min (1) | 0 → ValueError | 1 → Accepted | 2 → Accepted | ValueError / Accepted / Accepted |
| Max (50) | 49 → Accepted | 50 → Accepted | 51 → ValueError | Accepted / Accepted / ValueError |

**Total cases: 6**
**Test file:** `tests/test_validate_name.py` (function `test_validate_name_length_boundaries`)

---

## 4. Defect Found During Testing

While reviewing GradeBook for test coverage during Lab 6, a defect was
identified in the `Student` class: the `get_grade()` method was missing
entirely. This meant students had no way to obtain a letter grade derived
from their stored scores, even though the `letter_grade()` function already
existed at module level.

This was filed as **issue #15** and fixed via **PR #17** on a feature branch
named `fix/get-grade-method`, using the standard Lab 2 branching workflow.

- **Detected by:** manual coverage review combined with EP + BVA test design
- **Filed as:** issue #15 — "Defect: Student object missing get_grade() method"
- **Fixed via:** PR #17 — `fix(student): add get_grade() method — Fixes #15`
- **Branch:** `fix/get-grade-method`
- **Regression coverage:** `tests/test_get_grade.py` (8 cases covering all
  letter-grade boundaries F/D/C/B/A and the empty-scores edge case, all passing)
- **Auto-closed:** Merging PR #17 automatically closed issue #15 via the
  `Fixes #15` keyword.

---

## 5. EP + BVA Combined Suite — Final Status


tests/test_letter_grade.py 7 passed (Lab 5 EP)
tests/test_letter_grade_bva.py 18 passed (Lab 6 BVA)
tests/test_roster.py 9 passed (Lab 5 EP + Lab 6 BVA)
tests/test_validate_name.py 10 passed (Lab 5 EP + Lab 6 BVA)
tests/test_get_grade.py 8 passed (regression, issue #15)

Total: 52 passed


- **EP tests** ensure each equivalence class works correctly.
- **BVA tests** ensure boundaries between classes are correct (off-by-one
  protection).
- **Regression test** locks in the fix for the missing `get_grade()` defect.

Together they provide strong, layered coverage for the three functions under
test plus the `Student` class.
- **BVA tests** ensure boundaries between classes are correct.
- Together they provide strong coverage for the three functions under test.
