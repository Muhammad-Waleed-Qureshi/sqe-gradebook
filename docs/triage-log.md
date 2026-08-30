# Triage Log

## Issue Prioritization

| Rank | Issue | Defect                                       | Severity | Priority | Decision          |
| ---- | ----- | -------------------------------------------- | -------- | -------- | ----------------- |
| 1    | #1    | `average()` crashes with an empty score list | High     | P1       | Fix this sprint   |
| 2    | #2    | Negative scores are accepted                 | High     | P1       | Fix this sprint   |
| 3    | #3    | Duplicate roll numbers are allowed           | Medium   | P2       | Fix this sprint   |
| 4    | #4    | Average calculation uses incorrect rounding  | Medium   | P2       | Defer this sprint |
| 5    | #5    | Student name comparison is case-sensitive    | Low      | P3       | Defer this sprint |

## Triage Rationale

Issue #1 is ranked first because the crash affects a core gradebook operation and can stop the program from calculating an average. Issue #2 is ranked second because accepting negative scores can introduce invalid data and affect student grades. Issue #3 is ranked third because duplicate roll numbers can cause problems when identifying student records.

Issue #4 has Medium severity and P2 priority, but it is deferred because the system can still process scores even though the displayed average may be inaccurate. Issue #5 has Low severity and P3 priority because it mainly affects usability and does not corrupt data or crash the system.

The severity and priority are not always identical. For example, Issue #4 has Medium severity because it affects grade accuracy, but it is P2 because the system remains usable. Issue #5 has Low severity and P3 priority because the impact is mainly limited to name-based searching and can be addressed later.

## Sprint Decision

The three highest-priority issues (#1, #2, and #3) will be fixed during this sprint. Issues #4 and #5 will not be fixed this sprint because they have lower urgency compared with the other defects.
