import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import Student


# ---------- Regression test for issue #15 ----------
# Student.get_grade() should return the letter grade for the average.

@pytest.mark.parametrize("scores,expected_grade", [
    ([], "F"),              # empty -> average 0.0 -> F
    ([45], "F"),
    ([65], "D"),
    ([75], "C"),
    ([85], "B"),
    ([95], "A"),
    ([90, 92, 88], "A"),    # average 90 -> A
    ([59, 61], "D"),        # average 60 -> D
])
def test_student_get_grade(scores, expected_grade):
    s = Student("Ali", 101)
    for score in scores:
        s.add_score(score)
    assert s.get_grade() == expected_grade
