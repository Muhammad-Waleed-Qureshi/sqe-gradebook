# Triage Log

## Issue Prioritization

| Rank | Issue | Defect | Severity | Priority | Decision | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | #3 | `average()` crashes with an empty score list | High | P1 | Fix this sprint | Closed |
| 2 | #4 | Negative scores are accepted | High | P1 | Fix this sprint | Closed |
| 3 | #5 | Duplicate roll numbers are allowed | Medium | P2 | Fix this sprint | Closed |
| 4 | #6 | Average calculation uses incorrect rounding | Medium | P2 | Defer this sprint | Wontfix |
| 5 | #7 | Student name comparison is case-sensitive | Low | P3 | Defer this sprint | Wontfix |

---

## Triage Rationale

* **Issue #3** is ranked first because the crash affects a core gradebook operation and can stop the program from calculating an average. 
* **Issue #4** is ranked second because accepting negative scores can introduce invalid data and affect student grades. 
* **Issue #5** is ranked third because duplicate roll numbers can cause problems when identifying student records.
* **Issue #6** has Medium severity and P2 priority, but it is deferred because the system can still process scores even though the displayed average may be inaccurate. 
* **Issue #7** has Low severity and P3 priority because it mainly affects usability and does not corrupt data or crash the system.

The severity and priority are not always identical. For example, Issue #6 has Medium severity because it affects grade accuracy, but it is P2 because the system remains usable. Issue #7 has Low severity and P3 priority because the impact is mainly limited to name-based searching and can be addressed later.

---

## Sprint Decision

The three highest-priority issues (#3, #4, and #5) were fixed and closed during this sprint. Issues #6 and #7 will not be fixed this sprint because they have lower urgency compared with the other defects.
