import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gradebook.gradebook import Student, Roster

def test_class_average_empty_roster():
    """Test that an empty roster returns a class average of 0.0."""
    roster = Roster()
    assert roster.class_average() == 0.0

def test_class_average_single_student():
    """Test class average with a single student in the roster."""
    roster = Roster()
    student = Student("Ali", 101)
    student.add_score(80)
    student.add_score(90)  # average is 85.0
    roster.add_student(student)
    
    assert roster.class_average() == 85.0

def test_class_average_multiple_students():
    """Test class average with multiple students in the roster."""
    roster = Roster()
    
    s1 = Student("Ali", 101)
    s1.add_score(80) # average 80
    
    s2 = Student("Sara", 102)
    s2.add_score(100) # average 100
    
    roster.add_student(s1)
    roster.add_student(s2)
    
    # Average of (80 + 100) / 2 = 90.0
    assert roster.class_average() == 90.0
