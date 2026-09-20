# Test Cases

## GradeBook Test Cases

| TC ID | Test Case | Req | Preconditions | Test Steps | Expected Result | Priority | Type | Execution Result | Issue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-001 | Add valid score | REQ-1 | Student created | Call `student.add_score(85)`. | Score added successfully. | High | Functional | **FAIL** — No `add_score()`. | #13 |
| TC-002 | Reject negative score | REQ-1 | Student created | Call `student.add_score(-10)`. | Raises `ValueError`. | High | Negative | **FAIL** — No `add_score()`. | #13 |
| TC-003 | Reject non-numeric score | REQ-1 | Student created | Call `student.add_score("abc")`. | Raises error. | Medium | Negative | **FAIL** — No `add_score()`. | #13 |
| TC-004 | Calculate average | REQ-2 | Scores: `[80, 90, 100]` | Call `student.average()`. | Returns `90.0`. | High | Functional | **PASS** — Returned `90`. | — |
| TC-005 | Average empty list | REQ-2 | Scores: `[]` | Call `student.average()`. | Returns `0.0`. | High | Edge Case | **PASS** — Returned `0`. | — |
| TC-006 | Average single score | REQ-2 | Scores: `[75]` | Call `student.average()`. | Returns `75.0`. | Medium | Functional | **PASS** — Returned `75`. | — |
| TC-007 | Duplicate roll number | REQ-3 | Roll `101` exists | Add duplicate roll `101`. | Raises `ValueError`. | High | Negative | **PASS** — Raised error. | — |
| TC-008 | Name search case-ins. | REQ-4 | Student `"Ali"` exists | Search using `"ali"`. | Finds record. | Low | Functional | **FAIL** — No `find_student()`. | #14 |
| TC-009 | Max score boundary | REQ-5 | Student created | Call `student.add_score(100)`. | Score accepted. | Medium | Boundary | **FAIL** — No `add_score()`. | #13 |
| TC-010 | Min score boundary | REQ-5 | Student created | Call `student.add_score(0)`. | Score accepted. | Medium | Boundary | **FAIL** — No `add_score()`. | #13 |
| TC-011 | Grade letter mid-range | REQ-6 | Average `82.0` | Call `student.get_grade()`. | Returns `'B'`. | Low | Functional | **FAIL** — No `get_grade()`. | #15 |
| TC-012 | Grade letter boundary | REQ-6 | Average `90.0` | Call `student.get_grade()`. | Returns `'A'`. | Low | Boundary | **FAIL** — No `get_grade()`. | #15 |

## Execution Summary

| Status | Count |
| :--- | :--- |
| Pass | 3 |
| Fail | 9 |
| Blocked | 0 |
| **Total** | **12** |

## Defect Summary

| Defect | Affected Test Cases | Defect Issue |
| :--- | :--- | :--- |
| Missing `Student.add_score()` | TC-001, TC-002, TC-003, TC-009, TC-010 | #13 |
| Missing `GradeBook.find_student()` | TC-008 | #14 |
| Missing `Student.get_grade()` | TC-011, TC-012 | #15 |


## Re-execution Note (after Lab 5 + Lab 6)

After implementing `add_score()` (Lab 5) and `get_grade()` (Lab 6,
issue #15 → PR #17), the following test cases were re-executed against
the updated codebase and now pass:

| TC ID | Old Result | New Result |
| :--- | :--- | :--- |
| TC-001 | FAIL | **PASS** |
| TC-002 | FAIL | **PASS** |
| TC-009 | FAIL | **PASS** |
| TC-010 | FAIL | **PASS** |
| TC-011 | FAIL | **PASS** |
| TC-012 | FAIL | **PASS** |

**Still failing:**
- **TC-003** — `add_score()` does not validate non-numeric input (raises `TypeError` instead of `ValueError`). Tracked as a follow-up defect.
- **TC-008** — `GradeBook.find_student()` is still not implemented. Tracked as issue #14.

**Updated Execution Summary (post-fix):**

| Status | Count |
| :--- | :--- |
| Pass | 9 |
| Fail | 2 |
| Blocked | 1 |
| **Total** | **12** |

