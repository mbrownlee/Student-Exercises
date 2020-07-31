DELETE FROM Cohort;
DELETE FROM Exercise;
DELETE FROM Instructor;
DELETE FROM Student;
DELETE FROM StudentExercises;

DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Instructor;
DROP TABLE IF EXISTS Cohort;
DROP TABLE IF EXISTS Exercise;
DROP TABLE IF EXISTS StudentExercises;


CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL UNIQUE
);


CREATE TABLE Student (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL, 
    SlackHandle TEXT NOT NULL,
    CohortId INTEGER NOT NULL,
    FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Instructor (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL, 
    SlackHandle TEXT NOT NULL,
    CohortId INTEGER NOT NULL,
    Specialty TEXT NOT NULL,
    FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Exercise (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Language TEXT NOT NULL

);

CREATE TABLE StudentExercises (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    StudentId INTEGER NOT NULL,
    ExerciseId INTEGER NOT NULL,
    FOREIGN KEY(StudentId) REFERENCES Student(Id),
    FOREIGN KEY(ExerciseId) REFERENCES Exercise(Id)
    
);

insert into Cohort
(Name)
Values ("Day Cohort 40");

insert into Cohort
(Name)
Values ("Day Cohort 41");

insert into Cohort
(Name)
Values ("Evening Cohort 16");

INSERT INTO Exercise (Name, Language) 
VALUES ("Kandy Korner", "React");

INSERT INTO Exercise (Name, Language) 
VALUES ("Keahua", "Python");

INSERT INTO Exercise (Name, Language) 
VALUES ("Kennel", "React");

INSERT INTO Exercise (Name, Language) 
VALUES ("Welcome to Nashville", "JavaScript");

INSERT INTO Exercise (Name, Language) 
VALUES ("Nutshell", "JavaScript");

SELECT * FROM Exercise;

iNSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty)
SELECT "Bryan", "Neilson", "BryFive", Cohort.Id, "Cheering students on"
from Cohort
where  Cohort.Name like "%40%";

iNSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty)
SELECT "Sage", "Houchens", "SageH", Cohort.Id, "Dark humor"
from Cohort
where  Cohort.Name like "%41%";

iNSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty)
SELECT "Madi", "Peper", "Madi", Cohort.Id, "Traffic reports"
from Cohort
where  Cohort.Name like "%16%";

select * from Instructor;

iNSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
SELECT "Hattie", "B", "Hot chicken", Cohort.Id
from Cohort
where  Cohort.Name like "%16%";

iNSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
SELECT "Mike", "Dancer", "Mikie", Cohort.Id
from Cohort
where  Cohort.Name like "%16%";

iNSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
SELECT "Adrian", "Gard", "Adrian", Cohort.Id
from Cohort
where  Cohort.Name like "%40%";

iNSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
SELECT "Roxanne", "Nast", "Roxie", Cohort.Id
from Cohort
where  Cohort.Name like "%40%";

iNSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
SELECT "Leigha", "Roberts", "Leigha", Cohort.Id
from Cohort
where  Cohort.Name like "%40%";

iNSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
SELECT "Sarah", "Jones", "Sarah", Cohort.Id
from Cohort
where  Cohort.Name like "%41%";

iNSERT INTO Student (FirstName, LastName, SlackHandle, CohortId)
SELECT "Dirk", "Dirt", "DD", Cohort.Id
from Cohort
where  Cohort.Name like "%41%";

SELECT * FROM Student;

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Mike" 
and Student.LastName = "Dancer"
and Exercise.Name = "Kandy Korner";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Mike" 
and Student.LastName = "Dancer"
and Exercise.Name = "Kennel";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Hattie" 
and Student.LastName = "B"
and Exercise.Name = "Kennel";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Hattie" 
and Student.LastName = "B"
and Exercise.Name = "Welcome to Nashville";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Adrian" 
and Student.LastName = "Gard"
and Exercise.Name = "Welcome to Nashville";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Adrian" 
and Student.LastName = "Gard"
and Exercise.Name = "Nutshell";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Roxanne" 
and Student.LastName = "Nast"
and Exercise.Name = "Keahua";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Roxanne" 
and Student.LastName = "Nast"
and Exercise.Name = "Nutshell";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Leigha" 
and Student.LastName = "Roberts"
and Exercise.Name = "Kennel";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Leigha" 
and Student.LastName = "Roberts"
and Exercise.Name = "Kandy Korner";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Sarah" 
and Student.LastName = "Jones"
and Exercise.Name = "Kandy Korner";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Sarah" 
and Student.LastName = "Jones"
and Exercise.Name = "Keahua";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Dirk" 
and Student.LastName = "Dirt"
and Exercise.Name = "Keahua";

INSERT INTO StudentExercises (StudentId, ExerciseId)
select Student.Id, Exercise.Id
from Student, Exercise
where Student.FirstName = "Dirk" 
and Student.LastName = "Dirt"
and Exercise.Name = "Welcome to Nashville";

select * from StudentExercises;








