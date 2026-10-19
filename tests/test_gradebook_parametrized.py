import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import letter_grade

@pytest.mark.parametrize(
    "score, expected",
    [
        (95, "A"),
        (90, "A"),
        (89, "B"),
        (80, "B"),
        (79, "C"),
        (70, "C"),
        (69, "D"),
        (60, "D"),
        (59, "F"),
        (0, "F"),
    ],
)
def test_letter_grade_parametrized(score, expected):
    """Test letter_grade mapping across various grade boundaries using parametrization."""
    assert letter_grade(score) == expected

@pytest.mark.parametrize(
    "invalid_score",
    [
        -1,
        101,
        "90",
        None,
        True,
    ],
)
def test_letter_grade_invalid_raises_value_error(invalid_score):
    """Test that invalid scores or data types correctly raise a ValueError."""
    with pytest.raises(ValueError):
        letter_grade(invalid_score)
