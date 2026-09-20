class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.scores = []

    def average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)


    def get_grade(self):
        """Return the letter grade for this student's average score."""
        return letter_grade(self.average())
    
    def add_score(self, score):
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(score)


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for existing in self.students:
            if existing.roll_no == student.roll_no:
                raise ValueError("Roll number already exists")
        self.students.append(student)


# ---------- Lab 5 additions ----------

def letter_grade(score):
    """Map a numeric score (0-100) to a letter grade A-F."""
    if not isinstance(score, (int, float)) or isinstance(score, bool):
        raise ValueError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def validate_name(name):
    """Validate a student name: non-empty, <=50 chars, letters/spaces/hyphens only."""
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    cleaned = name.strip()
    if len(cleaned) == 0:
        raise ValueError("Name must not be empty")
    if len(cleaned) > 50:
        raise ValueError("Name must be 50 characters or fewer")
    for ch in cleaned:
        if not (ch.isalpha() or ch in (" ", "-")):
            raise ValueError("Name may only contain letters, spaces, hyphens")
    return cleaned


class Roster:
    """A collection of students; each must have 1-6 scores."""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Only Student instances may be added")
        n = len(student.scores)
        if n < 1 or n > 6:
            raise ValueError("Student must have between 1 and 6 scores")
        self.students.append(student)
