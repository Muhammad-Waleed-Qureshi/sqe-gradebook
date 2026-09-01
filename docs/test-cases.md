# Test Cases Specification: GradeBook Module

| ID | Title | Requirement | Preconditions | Steps | Expected Result | Priority | Type | Execution Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-001** | Add valid score | REQ-1 | Student object created with empty scores list | 1. Call `student.add_score(85)` | Score `85` is added successfully to the list | High | Functional | Pass |
| **TC-002** | Reject negative score | REQ-1 | Student object created | 1. Call `student.add_score(-10)` | Raises `ValueError` and scores list remains unchanged | High | Negative / Functional | Pass |
| **TC-003** | Reject non-numeric score | REQ-1 | Student object created | 1. Call `student.add_score("abc")` | Raises `TypeError` or `ValueError` | Medium | Negative / Functional | Pass |
| **TC-004** | Calculate average with scores | REQ-2 | Student has scores `[80, 90, 100]` | 1. Call `student.average()` | Returns correct average `90.0` | High | Functional | Pass |
| **TC-005** | Average with empty list | REQ-2 | Student has an empty scores list `[]` | 1. Call `student.average()` | Returns `0.0` without crashing (`ZeroDivisionError` handled) | High | Negative / Edge Case | Pass |
| **TC-006** | Average with single score | REQ-2 | Student has a single score `[75]` | 1. Call `student.average()` | Returns `75.0` | Medium | Functional | Pass |
| **TC-007** | Duplicate roll number rejection | REQ-3 | GradeBook catalog already contains roll number `101` | 1. Add another student with roll number `101` | Raises `ValueError` to prevent duplicates | High | Negative / Functional | Pass |
| **TC-008** | Name case-insensitivity search | REQ-4 | Student named "Ali" exists in system | 1. Search student using lowercase `"ali"` | System successfully finds and returns the student record | Low | Functional | Pass |
| **TC-009** | Maximum score boundary (100) | REQ-5 | Student object created | 1. Call `student.add_score(100)` | Score `100` is accepted successfully | Medium | Boundary | Pass |
| **TC-010** | Minimum score boundary (0) | REQ-5 | Student object created | 1. Call `student.add_score(0)` | Score `0` is accepted successfully | Medium | Boundary | Pass |
| **TC-011** | Grade letter mid-range score | REQ-6 | Student average is `82.0` | 1. Call `student.get_grade()` | Returns grade letter `'B'` | Low | Functional | Pass |
| **TC-012** | Grade letter at exact boundary | REQ-6 | Student average is exactly `90.0` | 1. Call `student.get_grade()` | Returns top grade letter `'A'` | Low | Boundary | Pass |
