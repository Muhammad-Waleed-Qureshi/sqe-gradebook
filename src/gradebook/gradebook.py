
from importlib.resources import path

class GradeBookIOError(Exception):
    """Raised when saving the roster fails."""
=======
class GradeBookIOError(Exception):
    """Custom exception raised for file I/O failures in the GradeBook system."""
    pass



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
        return letter_grade(self.average())

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")

        self.scores.append(score)


        self.scores.append(score)

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for existing in self.students:
            if existing.roll_no == student.roll_no:
                raise ValueError("Roll number already exists")
        self.students.append(student)



def letter_grade(score):
   
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

    def __init__(self):
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Only Student instances may be added")
        n = len(student.scores)
        if n < 1 or n > 6:
            raise ValueError("Student must have between 1 and 6 scores")
        self.students.append(student)


    
    def save_to_file(self, path):
        try:
            file = open(path, "w", encoding="utf-8")

            for student in self.students:
                file.write(f"{student.name},{student.roll_no}\n")

            file.close()

        except OSError as exc:
                raise GradeBookIOError("Could not save roster") from exc

        
    def class_average(self):
        if not self.students:
            return 0.0

        total = 0

        for student in self.students:
            total += student.average()

        return total / len(self.students)


    def class_average(self):
        """Calculate the average of all students' averages in the roster[cite: 5]."""
        if not self.students:
            return 0.0
        total = sum(student.average() for student in self.students)
        return total / len(self.students)

    def save_to_file(self, path):
        """Write student records to disk, raising GradeBookIOError on failure[cite: 5]."""
        try:
            with open(path, "w") as f:
                for student in self.students:
                    f.write(f"{student.roll_no},{student.name},{student.average()}\n")
        except OSError as e:
            raise GradeBookIOError(f"Failed to save roster to file: {e}") from e

