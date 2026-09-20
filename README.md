# SQE Gradebook

SQE Gradebook is a small Python library for managing student records and
computing grade statistics. It stores students with a name and roll number,
tracks their scores, and provides utilities to compute averages, convert
numeric averages to letter grades, validate name inputs, and enforce roster
rules. The project is developed as part of the Software Quality Engineering
(SUE) lab series and grows one SQE discipline at a time — from repository
setup and branching (Labs 1–2), through defect management and test planning
(Labs 3–4), to black-box test design using Equivalence Partitioning and
Boundary Value Analysis (Labs 5–6).

## Features

- `Student` — name, roll number, scores, `average()`, `add_score()`,
  `get_grade()`
- `GradeBook` / `Roster` — collections of students with duplicate roll-number
  prevention and score-count rules
- `letter_grade(score)` — maps a numeric score (0–100) to a letter A–F
- `validate_name(name)` — enforces name rules (non-empty, ≤50 chars,
  letters/spaces/hyphens only)

## Installation

Clone the repository and install the required dependencies:

```bash
git clone git@github.com:Muhammad-Waleed-Qureshi/sqe-gradebook.git
cd sqe-gradebook
pip install -r requirements.txt
