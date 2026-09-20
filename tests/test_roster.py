import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import Student, Roster


# ---------- Lab 5: Equivalence Partitioning ----------
# Rule: 1-6 scores valid. Classes: 0 (invalid), 3 (valid), 8 (invalid).

@pytest.mark.parametrize("num_scores,should_pass", [
    (0, False),
    (3, True),
    (8, False),
])
def test_roster_score_count_classes(num_scores, should_pass):
    r = Roster()
    s = Student("Ali", 101)
    s.scores = [50] * num_scores
    if should_pass:
        r.add_student(s)
        assert s in r.students
    else:
        with pytest.raises(ValueError):
            r.add_student(s)


# ---------- Lab 6: Boundary Value Analysis ----------
# Boundaries at 0/1 and 6/7.

@pytest.mark.parametrize("num_scores,should_pass", [
    (0, False),   # min-1 -> invalid
    (1, True),    # min valid
    (2, True),    # min+1
    (5, True),    # max-1
    (6, True),    # max valid
    (7, False),   # max+1 -> invalid
])
def test_roster_score_count_boundaries(num_scores, should_pass):
    r = Roster()
    s = Student("Ali", 101)
    s.scores = [50] * num_scores
    if should_pass:
        r.add_student(s)
        assert s in r.students
    else:
        with pytest.raises(ValueError):
            r.add_student(s)
