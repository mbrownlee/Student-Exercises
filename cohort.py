class Cohort:

    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()

    def __str__(self):
        return f"{self.name}"

    def addStudents(self, students):
        self.students.extend(students)

    def addInstructors(self, instructors):
        self.instructors.extend(instructors)

