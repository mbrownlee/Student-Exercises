from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

kennel = Exercise("Kennel", "React")
kandy_korner = Exercise("Kandy Korner", "React")
c_m = Exercise("Chicken Monkey", "JavaScript")
critters = Exercise("Critters and Croquettes", "Python")

exercises = [kennel, kandy_korner, c_m, critters]
for work in exercises:
    print(f"{work.name} stresses the {work.language} language.")

c40 = Cohort("Cohort day 40")
c41 = Cohort("Cohort day 41")
c10 = Cohort("Cohort evening 10 ")

joe = Student("Joe", "Dirt", "joe_dirt", c10)
jane = Student("Jane", "Ball", "jane_awesome", c41)
mike = Student("Mike", "Wolf", "wolfman", c40)
marge = Student("Marge", "Simpsom", "bluehair", c41)

mike.full_name
joe.full_name
jane.full_name
marge.full_name

students = [joe, jane, mike, marge]
for person in students:
    print(f" * {person.first_name} {person.last_name}")

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
steve.add_exercises(mike, [critters, c_m])

for exer in mike.exercise:
    print(f"Mike is currently working on {exer.name}.")


# for student in students:
#     print(f'{student.first_name} {student.last_name} is currently working on')
#     empty=""
#     for work in student.exercise:
#         empty+= work.name + " and "
#     print(empty)

def printout():
    for student in students:
        exercises = []
        for exercise in student.exercise:
            exercises.append(exercise.name)
        print(f"{student.first_name} {student.last_name} is currently working on {' and '.join(exercises)}.")


printout()















