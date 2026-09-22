import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest

from gradebook.gradebook import Student


def test_add_score_rejects_score_above_100():
    student = Student("Ali", 101)

    with pytest.raises(ValueError):
        student.add_score(101)


def test_add_score_rejects_negative_score():
    student = Student("Ali", 101)

    with pytest.raises(ValueError):
        student.add_score(-1)


def test_add_score_accepts_valid_score():
    student = Student("Ali", 101)

    student.add_score(100)

    assert student.scores == [100]