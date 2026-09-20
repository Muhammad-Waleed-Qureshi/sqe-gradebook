import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import Student, Roster


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
