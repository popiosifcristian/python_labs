from Domain.Note import Note
from Repository import Repositories


class Controller:
    """
    This class contains last functionality that our application requires.
    (e.g. filters, searching for specific fields, etc)
    """

    def __init__(self):
        """
        The default constructor for the Controller class that contains the initialization of the repositories.
        """
        self.repositories = Repositories.Repositories()

    def list_students(self):
        """
        This method will print all the students from the repository.
        """
        students = self.repositories.student_repository.get_all()
        for student in students:
            print(student)

    def list_disciplines(self):
        """
        This method will print all the disciplines from the repository.
        """
        disciplines = self.repositories.discipline_repository.get_all()
        for discipline in disciplines:
            print(discipline)

    @staticmethod
    def list_notes(notes):
        """
        This method will print all the disciplines from the repository.
        """
        for note in notes:
            print(note)

    def filter_students_by_name(self, name):
        """
        This method will filter the student repository by an specific student name.
        :param name: Received name for the filtering.
        :return: All students with the specific name.
        """
        students = []
        if name is not None:
            for student in self.repositories.student_repository.get_all():
                if name == student.get_name() or name in student.get_name():
                    students.append(student)
        return students

    def filter_disciplines_by_name(self, name):
        """
        This method will filter the discipline repository by an specific discipline name.
        :param name: Received name for the filtering.
        :return: All disciplines with the specific name.
        """
        disciplines = []
        if name is not None:
            for discipline in self.repositories.discipline_repository.get_all():
                if name == discipline.get_name() or name in discipline.get_name():
                    disciplines.append(discipline)
        return disciplines

    def __filter_notes_by_discipline(self, discipline):
        """
        This method will filter all notes by a specific discipline.
        :param discipline: Received discipline for the filtering.
        :return: All notes with the specific discipline.
        """
        notes = []
        if discipline is not None:
            for note in self.repositories.note_repository.get_all():
                if discipline == note.get_discipline_name() or discipline in note.get_discipline_name():
                    notes.append(note)
        return notes

    def order_notes_by_student_name_and_discipline(self, discipline):
        """
        This method will order the notes by student name.
        :return: An ordered list with notes.
        """
        notes = self.__filter_notes_by_discipline(discipline)
        result = sorted(notes, key=Note.get_student_name, reverse=True)
        return result

    def order_notes_by_note_and_discipline(self, discipline):
        """
        This method will order the notes by student name.
        :return: An ordered list with notes.
        """
        notes = self.__filter_notes_by_discipline(discipline)
        result = sorted(notes, key=Note.get_note, reverse=True)
        return result

    @staticmethod
    def __get_notes_by_student(notes, student_name):
        """
        This method will iterate the notes list and will return all notes of the specific student.
        :param notes: The notes list.
        :param student_name: The specific student name for the search.
        :return: A list of notes that belongs to that specific student.
        """
        student_notes = []
        for note in notes:
            # if student_name == note.get_student_name() or student_name in note.get_student_name():
            if student_name == note.get_student_name():
                student_notes.append(note)
        return student_notes

    @staticmethod
    def __calculate_average(notes):
        """
        This method calculate the average of the notes list received.
        :param notes: The notes list.
        :return: Average of the notes.
        """
        notes_sum = 0
        for note in notes:
            notes_sum += note.get_note()
        return notes_sum / float(len(notes))

    def get_best_students(self):
        """
        This method return the best students from repository (first 20% students) ordered by their average of
        notes from all disciplines.
        :return: First 20% students ordered by their average on all disciplines.
        """
        initial_result = []
        final_result = []
        students = self.repositories.student_repository.get_all()
        notes = self.repositories.note_repository.get_all()
        no_of_students = len(students)
        first_students = int(round(no_of_students * 20 / 100))

        for student in students:
            average = self.__calculate_average(self.__get_notes_by_student(notes, student.get_name()))
            student_average = {'name': student.get_name(), 'average': average}
            initial_result.append(student_average)

        initial_result = sorted(initial_result, key=lambda tup: tup['average'], reverse=True)
        for index in range(0, first_students):
            final_result.append(initial_result[index])

        return final_result

    @staticmethod
    def list_best_students(best_students):
        """
        Specific print method for received list of best students dictionaries.
        :param best_students: Received list of dictionaries.
        """
        for student in best_students:
            print("Student: {0}, Average: {1}.".format(student['name'], student['average']))

    def update_student(self, student, new_name):
        """
        This method will update the student entity with the new name and will also update all his notes with
        the received new name.
        :param student: The student to be updated.
        :param new_name: The new name for the student.
        """
        notes = self.repositories.note_repository.get_all()

        for note in notes:
            if note.get_student_name() == student.get_name():
                note.set_student_name(new_name)
                self.repositories.note_repository.update(note)

        student.set_name(new_name)
        self.repositories.student_repository.update(student)

    def update_discipline_name(self, discipline, new_name):
        """
        This method will update the discipline entity with the new name and will also update all his notes with
        the received new name.
        :param discipline: The student to be updated.
        :param new_name: The new name for the student.
        """
        notes = self.repositories.note_repository.get_all()

        for note in notes:
            if note.get_discipline_name() == discipline.get_name():
                note.set_discipline_name(new_name)
                self.repositories.note_repository.update(note)

        discipline.set_name(new_name)
        self.repositories.discipline_repository.update(discipline)


class Validator:
    """
    This class contains all the validations for the UI layer of the application.
    """

    @staticmethod
    def check_int(number):
        """
        This method checks if the received string is a digit.
        :param number: The string to be checked
        :return: True if the received string is a digit, otherwise False.
        """
        if number.isdigit() is False:
            return False
        return True

    def validate_int(self, number):
        """
        This methods checks if the received string is an int, if its not it will continuous ask for an int.
        :param number: The received string to be checked.
        :return: Received string converted to int.
        """
        while self.check_int(number) is False:
            number = input("Please enter an digit: ")
        return int(number)

    @staticmethod
    def check_positive(number):
        """
        This method checks if the received number is positive.
        :param number: The number to be checked
        :return: True if the received number is positive, otherwise False.
        """
        if number < 0:
            return False
        return True

    @staticmethod
    def check_float(number):
        """
        This method checks if the received string is a float.
        :param number: The string to be checked
        :return: True if the received string is a float, otherwise False.
        """
        try:
            float(number)
        except ValueError:
            return False
        return True

    def validate_note(self, note):
        """
        This method will check if the received note is valid, if is not valid, it will loop until
        the user enter a valid note.
        :param note: The note to be checked.
        :return: A valid note.
        """
        while self.check_float(note) is False or 0 > float(note) or float(note) > 10:
            note = input("Enter a valid note(a number between 0 and 10): ")
        return note
