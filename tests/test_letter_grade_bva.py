import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import letter_grade


# ---------- Domain edges: -1, 0, 1, 99, 100, 101 ----------

@pytest.mark.parametrize("score,expected", [
    (-1, None),   # below min -> ValueError
    (0, "F"),     # min valid
    (1, "F"),     # min+1
    (99, "A"),    # max-1
    (100, "A"),   # max valid
    (101, None),  # above max -> ValueError
])
def test_letter_grade_domain_edges(score, expected):
    if expected is None:
        with pytest.raises(ValueError):
            letter_grade(score)
    else:
        assert letter_grade(score) == expected


# ---------- F/D boundary: 59/60/61 ----------

@pytest.mark.parametrize("score,expected", [
    (59, "F"),
    (60, "D"),
    (61, "D"),
])
def test_letter_grade_boundary_F_D(score, expected):
    assert letter_grade(score) == expected


# ---------- D/C boundary: 69/70/71 ----------

@pytest.mark.parametrize("score,expected", [
    (69, "D"),
    (70, "C"),
    (71, "C"),
])
def test_letter_grade_boundary_D_C(score, expected):
    assert letter_grade(score) == expected


# ---------- C/B boundary: 79/80/81 ----------

@pytest.mark.parametrize("score,expected", [
    (79, "C"),
    (80, "B"),
    (81, "B"),
])
def test_letter_grade_boundary_C_B(score, expected):
    assert letter_grade(score) == expected


# ---------- B/A boundary: 89/90/91 ----------

@pytest.mark.parametrize("score,expected", [
    (89, "B"),
    (90, "A"),
    (91, "A"),
])
def test_letter_grade_boundary_B_A(score, expected):
    assert letter_grade(score) == expected


