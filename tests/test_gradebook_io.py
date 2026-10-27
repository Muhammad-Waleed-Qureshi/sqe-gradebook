import sys
import os

sys.path.insert(0, os.path.join(path := os.path.dirname(__file__), "..", "src"))

import pytest
from unittest.mock import patch, mock_open
from gradebook.gradebook import Student, Roster, GradeBookIOError

def test_save_to_file_success():
    """Test that roster successfully writes student data to a file using mock."""
    roster = Roster()
    student = Student("Ali", 101)
    student.add_score(85)
    roster.add_student(student)

    # Mock the built-in open function
    m = mock_open()
    with patch("builtins.open", m):
        roster.save_to_file("dummy_path.txt")

    # Verify open was called correctly and data was written
    m.assert_called_once_with("dummy_path.txt", "w")
    m().write.assert_called_once_with("101,Ali,85.0\n")

def test_save_to_file_io_error():
    """Test that save_to_file raises GradeBookIOError when an OS/IO error occurs."""
    roster = Roster()
    student = Student("Sara", 102)
    student.add_score(90)
    roster.add_student(student)

    # Force open() to raise an OSError
    with patch("builtins.open", side_effect=OSError("Disk full")):
        with pytest.raises(GradeBookIOError) as exc_info:
            roster.save_to_file("invalid_path.txt")
        
        assert "Failed to save roster to file" in str(exc_info.value)
