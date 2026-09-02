# Requirements Traceability Matrix (RTM): GradeBook Module

This matrix maps each functional requirement of the GradeBook project to its corresponding Test Case IDs to ensure complete test coverage and trace any validation gaps.

| Requirement ID | Requirement Description | Linked Test Case IDs | Coverage Status |
| :--- | :--- | :--- | :--- |
| **REQ-1** | The system shall validate scores (accept valid, reject negative/non-numeric). | TC-001, TC-002, TC-003 | Fully Covered |
| **REQ-2** | The system shall compute accurate grade averages, handling empty lists safely. | TC-004, TC-005, TC-006 | Fully Covered |
| **REQ-3** | The system shall prevent duplicate student roll numbers in the catalog. | TC-007 | Fully Covered |
| **REQ-4** | Student search and identification features shall be case-insensitive. | TC-008 | Fully Covered |
| **REQ-5** | The system shall enforce valid score boundaries (between 0 and 100). | TC-009, TC-010 | Fully Covered |
| **REQ-6** | The system shall correctly convert student numeric averages into letter grades. | TC-011, TC-012 | Fully Covered |

---

## Traceability Audit & Gap Analysis

* **Total Requirements Defined:** 6
* **Total Test Cases Mapped:** 12
* **Initial Gap Identification:** During the preliminary audit, any unmapped features (such as boundary handling and case-insensitivity) were flagged as potential gaps.
* **Gap Closure Action:** Test cases TC-008, TC-009, TC-010, TC-011, and TC-012 were specifically added to close all boundary and search-related coverage gaps.
* **Final Status:** 0 untraced requirements remaining. All functional requirements have at least one verifying test case.
