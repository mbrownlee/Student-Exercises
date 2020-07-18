from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

kennel = Exercise("Kennel", "React")
kandy_korner = Exercise("Kandy Korner", "React")
c_m = Exercise("Chicken Monkey", "JavaScript")
critters = Exercise("Critters and Croquettes", "Python")

c40 = Cohort("Cohort day 40")
c41 = Cohort("Cohort day 41")
c10 = Cohort("Cohort evening 10 ")

joe = Student("Joe", "Dirt", "joe_dirt", c10)
jane = Student("Jane", "Ball", "jane_awesome", c41)
mike = Student("Mike", "Wolf", "wolfman", c40)
marge = Student("Marge", "Simpsom", "bluehair", c41)

sage = Instructor("Sage", "Houchens", "mshouchens", "dry humor", c10)
bryan = Instructor("Bryan", "Neilsen", "hiBry", "high fives", c40)
steve = Instructor("Steve", "Brownlee", "coach", "dad jokes", c41)

c10.students.extend([joe, ])
c40.students.extend([mike, ])
c41.students.extend([marge, jane])

c10.instructors.extend([sage])
c40.instructors.extend([bryan])
c41.instructors.extend([steve])

print(mike)
sage.add_exercises(marge, [kennel, kandy_korner])
bryan.add_exercises(joe, [kennel, c_m])
steve.add_exercises(jane, [critters, c_m])
print(joe.exercises)













