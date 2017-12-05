from Repository import AbstractRepository
from Domain import Student, Discipline, Note


class Repositories:
    """
    This class contains all the repositories and the initialization with some objects of the repositories.
    """

    def __init__(self):
        """
        The default constructor of the Repositories class that contains the initialization of repositories and
        stockpiling of some objects.
        """
        self.student_repository = AbstractRepository.AbstractRepository()
        self.discipline_repository = AbstractRepository.AbstractRepository()
        self.note_repository = AbstractRepository.AbstractRepository()
        self.initialize_repositories()

    def initialize_repositories(self):
        """
        This method initialize the repositories with some objects.
        """
        discipline_1 = Discipline.Discipline("Discipline 1", "Teacher 1", 1)
        discipline_2 = Discipline.Discipline("Discipline 2", "Teacher 2", 2)
        self.discipline_repository.add(discipline_1)
        self.discipline_repository.add(discipline_2)

        student_1 = Student.Student("Student 1", 1)
        student_2 = Student.Student("Student 2", 2)
        student_3 = Student.Student("Student 3", 3)
        student_4 = Student.Student("Student 4", 4)
        student_5 = Student.Student("Student 5", 5)
        student_6 = Student.Student("Student 6", 6)
        student_7 = Student.Student("Student 7", 7)
        student_8 = Student.Student("Student 8", 8)
        student_9 = Student.Student("Student 9", 9)
        student_10 = Student.Student("Student 10", 10)
        self.student_repository.add(student_1)
        self.student_repository.add(student_2)
        self.student_repository.add(student_3)
        self.student_repository.add(student_4)
        self.student_repository.add(student_5)
        self.student_repository.add(student_6)
        self.student_repository.add(student_7)
        self.student_repository.add(student_8)
        self.student_repository.add(student_9)
        self.student_repository.add(student_10)

        self.note_repository.add(Note.Note("Student 1", "Discipline 1", 9))
        self.note_repository.add(Note.Note("Student 2", "Discipline 2", 7))
        self.note_repository.add(Note.Note("Student 3", "Discipline 1", 10))
        self.note_repository.add(Note.Note("Student 4", "Discipline 1", 5))
        self.note_repository.add(Note.Note("atudent 5", "Discipline 1", 5))
        self.note_repository.add(Note.Note("Student 6", "Discipline 1", 5))
        self.note_repository.add(Note.Note("Student 7", "Discipline 1", 5))
        self.note_repository.add(Note.Note("Student 8", "Discipline 1", 5))
        self.note_repository.add(Note.Note("Student 9", "Discipline 1", 5))
        self.note_repository.add(Note.Note("Student 10", "Discipline 1", 5))
        self.note_repository.add(Note.Note("Student 1", "Discipline 2", 10))
        self.note_repository.add(Note.Note("Student 2", "Discipline 2", 9))
        self.note_repository.add(Note.Note("Student 3", "Discipline 2", 8))
        self.note_repository.add(Note.Note("Student 4", "Discipline 2", 5))
        self.note_repository.add(Note.Note("Student 5", "Discipline 2", 5))
        self.note_repository.add(Note.Note("Student 6", "Discipline 2", 5))
        self.note_repository.add(Note.Note("Student 7", "Discipline 2", 5))
        self.note_repository.add(Note.Note("Student 8", "Discipline 2", 5))
        self.note_repository.add(Note.Note("Student 9", "Discipline 2", 5))
        self.note_repository.add(Note.Note("Student 10", "Discipline 2", 5))
