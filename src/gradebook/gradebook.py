class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.scores = []

    def average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)
