
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import Student, Roster


@pytest.fixture
def populated_roster():
    roster = Roster()

    ali = Student("Ali", 101)
    ali.add_score(80)
    ali.add_score(90)

    sara = Student("Sara", 102)
    sara.add_score(70)

    roster.add_student(ali)
    roster.add_student(sara)

    return roster


def test_empty_roster():
    roster = Roster()
    assert roster.class_average() == 0.0


def test_single_student():
    roster = Roster()
    ali = Student("Ali", 101)
    ali.add_score(80)
    ali.add_score(90)
    roster.add_student(ali)

    assert roster.class_average() == 85.0


def test_multiple_students(populated_roster):
    assert populated_roster.class_average() == pytest.approx(77.5)
