class NSSPerson():
    def __init__(self, first, last, slack, cohort):

        self.first_name = first
        self.last_name = last
        self.slack_handle = slack
        self.cohort = cohort
    
    @property
    def full_name(self):
        print(f"{self.first_name} {self.last_name}")