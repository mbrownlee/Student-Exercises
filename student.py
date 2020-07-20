from person import NSSPerson

class Student(NSSPerson):

    def __init__(self, first, last, slack, cohort ):
        super().__init__(first, last, slack, cohort)
        self.exercise = list()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.slack_handle} on slack, is a student in {self.cohort}."





