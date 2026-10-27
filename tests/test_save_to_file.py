
import sys
import os
from unittest.mock import mock_open, patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import Student, Roster, GradeBookIOError


def test_save_to_file_success():
    roster = Roster()
    student = Student("Ali", 101)
    student.add_score(80)
    roster.add_student(student)

    fake_file = mock_open()

    with patch("builtins.open", fake_file):
        roster.save_to_file("students.txt")

    fake_file.assert_called_once_with(
        "students.txt", "w", encoding="utf-8"
    )
    fake_file().write.assert_called_once_with("Ali,101\n")


def test_save_to_file_failure():
    roster = Roster()

    with patch("builtins.open", side_effect=OSError("Disk error")):
        with pytest.raises(GradeBookIOError, match="Could not save roster"):
            roster.save_to_file("students.txt")
