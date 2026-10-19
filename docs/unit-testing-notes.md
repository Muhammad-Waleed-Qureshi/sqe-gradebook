# Unit Testing Output & Traceback Notes

## 1. pytest -v (Verbose Mode)
- **Description:** Displays the full path and name of every individual test function along with its specific status (`PASSED`, `FAILED`, `SKIPPED`).
- **Use Case:** Best used during active local development or debugging when you need to see precisely which parametrized cases or test functions succeeded or failed at a granular level.

## 2. pytest --tb=short (Short Traceback Mode)
- **Description:** Suppresses verbose stack dumps and condenses failure tracebacks to the single line where the error occurred.
- **Use Case:** Best used in Continuous Integration (CI) pipelines or large test suites where full tracebacks create excessive log clutter, allowing developers to quickly pinpoint the failure origin.
