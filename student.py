class Student:

    def __init__(self, first, last, slack, cohort ):

        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.cohort = cohort
        self.exercise = list()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.slack_handle} on slack, is a student in {self.cohort}."





