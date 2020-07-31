from person import NSSPerson

class Instructor(NSSPerson):

    def __init__(self, first, last, slack, cohort, specialty):
        super().__init__(first, last, slack, cohort)
        self.speciality = specialty
        
    def add_exercises(self, student, exercise):
        student.exercise.extend(exercise)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.slack_handle} on slack, is a instructor in {self.cohort}."


      