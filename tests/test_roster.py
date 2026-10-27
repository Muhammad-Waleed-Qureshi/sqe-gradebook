import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import Student, Roster


# ---------- Lab 7: Fixtures Definition (Task 1) ----------

# Function-scoped fixture (default scope): 
# Yeh har test function ke liye ek naya Roster aur Student instance banata hai, 
# taaki test isolation maintain rahe aur ek test ka data doosre par asar na dale.
@pytest.fixture
def student_and_roster():
    r = Roster()
    s = Student("Ali", 101)
    return r, s


# Module-scoped fixture: 
# Yeh poore module me sirf ek baar run hota hai. 
# Ise wahan use kiya jata hai jahan setup heavy/expensive ho aur 
# read-only shared data multiple tests ko dena ho.
@pytest.fixture(scope="module")
def shared_module_setup():
    r = Roster()
    s = Student("Shared-Student", 999)
    return r, s


# ---------- Lab 5: Equivalence Partitioning ----------
# Rule: 1-6 scores valid. Classes: 0 (invalid), 3 (valid), 8 (invalid).

@pytest.mark.parametrize("num_scores,should_pass", [
    (0, False),
    (3, True),
    (8, False),
])
def test_roster_score_count_classes(num_scores, should_pass, student_and_roster):
    r, s = student_and_roster
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
def test_roster_score_count_boundaries(num_scores, should_pass, student_and_roster):
    r, s = student_and_roster
    s.scores = [50] * num_scores
    if should_pass:
        r.add_student(s)
        assert s in r.students
    else:
        with pytest.raises(ValueError):
            r.add_student(s)
