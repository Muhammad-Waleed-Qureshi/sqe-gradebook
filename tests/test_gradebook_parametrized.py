import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import Student, letter_grade

@pytest.mark.parametrize(
    "score, should_raise",
    [
        (85, False),
        (0, False),
        (100, False),
        (-1, True),
        (101, True),
        (50, False),
    ],
    ids=[
        "valid_mid_score",
        "valid_boundary_min",
        "valid_boundary_max",
        "invalid_below_min",
        "invalid_above_max",
        "valid_standard_score"
    ]
)
def test_add_score_parametrized(score, should_raise):
    """Consolidated parametrized test for student add_score method."""
    student = Student("Ali", 101)
    if should_raise:
        with pytest.raises(ValueError):
            student.add_score(score)
    else:
        student.add_score(score)
        assert score in student.scores
