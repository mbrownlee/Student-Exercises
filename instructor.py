class Instructor:

    def __init__(self, first, last, slack, cohort, specialty):

        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.cohort = cohort
        self.speciality = specialty
        
    def add_exercises(self, student, exercise):
        student.exercise.extend(exercise)


      