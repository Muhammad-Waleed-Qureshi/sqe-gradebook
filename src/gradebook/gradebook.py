class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.scores = []

    def average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)


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
