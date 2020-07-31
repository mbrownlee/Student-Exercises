import sqlite3
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/michelle/workspace/python/StudentExercises/studentexercises.db"

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)


    def all_instructors(self):
        """Retrieve all instrcutors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[4], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.FirstName,
                i.LastName,
                i.SlackHandle,
                i.CohortId,
                i.Specialty,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)

    def all_cohorts(self):
        """Retrieve all instrcutors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name
            from Cohort c
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)

    def all_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select ex.Id,
                ex.Name,
                ex.Language
            from Exercise ex
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    def all_javascript_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select ex.Id,
                ex.Name,
                ex.Language
            from Exercise ex
            where ex.Language like "%Java%"
            """)

            all_javascript_exercises = db_cursor.fetchall()

            for javascript_exercise in all_javascript_exercises:
                print(f'{javascript_exercise.name} is a {javascript_exercise.language} exercise.')

    def all_python_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select ex.Id,
                ex.Name,
                ex.Language
            from Exercise ex
            where ex.Language like "%Python%"
            """)

            all_python_exercises = db_cursor.fetchall()

            for python_exercise in all_python_exercises:
                print(f'{python_exercise.name} is a {python_exercise.language} exercise.')

    def all_react_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select ex.Id,
                ex.Name,
                ex.Language
            from Exercise ex
            where ex.Language like "%React%"
            """)

            all_react_exercises = db_cursor.fetchall()

            for react_exercise in all_react_exercises:
                print(f'{react_exercise.name} is a {react_exercise.language} exercise.')


reports = StudentExerciseReports()
reports.all_students()
reports.all_instructors()
reports.all_cohorts()
reports.all_exercises()
reports.all_javascript_exercises()
reports.all_python_exercises()
reports.all_react_exercises()


