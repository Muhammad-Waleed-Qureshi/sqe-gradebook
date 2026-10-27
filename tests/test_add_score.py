import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest

from gradebook.gradebook import Student


@pytest.mark.parametrize(
    "score, should_pass",
    [
        (0, True),
        (100, True),
        (50, True),
        (-1, False),
        (101, False),
        (75, True),
    ],
    ids=[
        "zero-score",
        "maximum-score",
        "valid-middle-score",
        "negative-score",
        "above-maximum",
        "another-valid-score",
    ],
)
def test_add_score(score, should_pass):
    student = Student("Ali", 101)

    if should_pass:
        student.add_score(score)
        assert student.scores == [score]
    else:
        with pytest.raises(ValueError):
            student.add_score(score)
