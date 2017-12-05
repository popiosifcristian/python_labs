import sys
from Controller import Controller
from Domain import Student, Discipline, Note


class UI:
    """
    This class contains the UI of the application.
    """

    def __init__(self):
        """
        The default constructor that contains the initialization of the controller and of the validator.
        """
        self.__controller = Controller.Controller()
        self.__validator = Controller.Validator()
        self.__student_id_index = 10
        self.__discipline_id_index = 2
        self.__note_id_index = 20

    __menu_variables = [
        "    ~~~Main Menu~~~ \n"
        "1.Student menu \n"
        "2.Discipline menu \n"
        "3.Note menu \n"
        "0.Exit \n",

        "    ~~~Student Menu~~~ \n"
        "1.Add student \n"
        "2.Update student \n"
        "3.Delete student \n"
        "4.Print students \n"
        "5.Find student by name \n"
        "9.Main menu \n"
        "0.Exit \n",

        "    ~~~Discipline Menu~~~ \n"
        "1.Add discipline \n"
        "2.Update discipline \n"
        "3.Delete discipline \n"
        "4.Print disciplines \n"
        "5.Find discipline by name \n"
        "9.Main menu \n"
        "0.Exit \n",

        "    ~~~Note menu~~~ \n"
        "1.Add Note \n"
        "2.Print discipline notes ordered alphabetical by student name \n"
        "3.Print discipline notes ordered descending by note \n"
        "4.Print best students ordered by the average of notes from all disciplines \n"
        "9.Main menu \n"
        "0.Exit \n",
    ]

    def main_menu(self):
        while True:
            print(self.__menu_variables[0])
            _choice = input("Your choice: ")
            _choice = self.__validator.validate_int(_choice)

            if _choice == 1:
                self.__student_menu()
                break
            elif _choice == 2:
                self.__discipline_menu()
                break
            elif _choice == 3:
                self.__note_menu()
                break
            if _choice == 0:
                sys.exit(0)
            else:
                print("Invalid option.")

    def __student_menu(self):
        while True:
            print(self.__menu_variables[1])
            _choice = input("Your choice: ")
            _choice = self.__validator.validate_int(_choice)

            if _choice == 1:
                self.__add_student()
            elif _choice == 2:
                self.__update_student()
            elif _choice == 3:
                self.__delete_student()
            elif _choice == 4:
                self.__print_students()
            elif _choice == 5:
                self.__find_student_by_name()
            elif _choice == 9:
                self.main_menu()
                break
            elif _choice == 0:
                sys.exit(0)
            else:
                print("Invalid option.")

    def __discipline_menu(self):
        while True:
            print(self.__menu_variables[2])
            _choice = input("Your choice: ")
            _choice = self.__validator.validate_int(_choice)

            if _choice == 1:
                self.__add_discipline()
            elif _choice == 2:
                self.__update_discipline()
            elif _choice == 3:
                self.__delete_discipline()
            elif _choice == 4:
                self.__print_disciplines()
            elif _choice == 5:
                self.__find_discipline_by_name()
            elif _choice == 9:
                self.main_menu()
                break
            elif _choice == 0:
                sys.exit(0)
            else:
                print("Invalid option.")

    def __note_menu(self):
        while True:
            print(self.__menu_variables[3])
            _choice = input("Your choice: ")
            _choice = self.__validator.validate_int(_choice)

            if _choice == 1:
                self.__add_note()
            elif _choice == 2:
                self.__get_notes_ordered_by_student_name_and_discipline()
            elif _choice == 3:
                self.__get_notes_by_note_and_discipline()
            elif _choice == 4:
                self.__get_best_students()
            elif _choice == 9:
                self.main_menu()
                break
            elif _choice == 0:
                sys.exit(0)

            else:
                print("Invalid option.")

    def __add_student(self):
        name = input("Name: ")
        self.__student_id_index += 1
        student = Student.Student(name, self.__student_id_index)
        self.__controller.repositories.student_repository.add(student)

    def __update_student(self):
        self.__controller.list_students()
        student_id = input("ID of the student to be updated: ")
        student_id = self.__validator.validate_int(student_id)
        student = self.__controller.repositories.student_repository.find_by_id(student_id)
        if student is None:
            print("No student found under ID: ", student_id)
        else:
            new_name = input("Enter new name for the student: ")
            self.__controller.update_student(student, new_name)

    def __delete_student(self):
        self.__controller.list_students()
        student_id = input("ID of the student to be deleted: ")
        student_id = self.__validator.validate_int(student_id)
        student = self.__controller.repositories.student_repository.find_by_id(student_id)
        if student is None:
            print("No student found under ID: ", student_id)
        else:
            self.__controller.repositories.student_repository.delete(student)

    def __print_students(self):
        self.__controller.list_students()

    def __find_student_by_name(self):
        name = input("Name: ")
        student_list = self.__controller.filter_students_by_name(name)
        if len(student_list) == 0:
            print("No students found under name: ", name)
        else:
            for student in student_list:
                print(student)

    def __add_discipline(self):
        name = input("Name: ")
        teacher_name = input("Teacher Name: ")
        self.__discipline_id_index += 1
        discipline = Discipline.Discipline(name, teacher_name, self.__discipline_id_index)
        self.__controller.repositories.discipline_repository.add(discipline)

    def __update_discipline(self):
        self.__controller.list_disciplines()
        discipline_id = input("ID of the discipline to be updated: ")
        discipline_id = self.__validator.validate_int(discipline_id)
        discipline = self.__controller.repositories.discipline_repository.find_by_id(discipline_id)
        if discipline is None:
            print("No discipline found under ID: ", discipline_id)
        else:
            print(" 1.Edit Name", '\n', "2.Edit Teacher Name \n")
            update_choice = input("Your choice: ")
            update_choice = self.__validator.validate_int(update_choice)
            if update_choice == 1:
                new_name = input("Enter new name: ")
                self.__controller.update_discipline_name(discipline, new_name)
            elif update_choice == 2:
                teacher_name = input("Enter new teacher name: ")
                discipline.set_teacher_name(teacher_name)
                self.__controller.repositories.discipline_repository.update(discipline)
            else:
                print("Invalid option.")

    def __delete_discipline(self):
        self.__controller.list_disciplines()
        discipline_id = input("ID of the discipline to be deleted: ")
        discipline_id = self.__validator.validate_int(discipline_id)
        discipline = self.__controller.repositories.discipline_repository.find_by_id(discipline_id)
        if discipline is None:
            print("No discipline found under ID: ", discipline_id)
        else:
            self.__controller.repositories.discipline_repository.delete(discipline)

    def __print_disciplines(self):
        self.__controller.list_disciplines()

    def __find_discipline_by_name(self):
        name = input("Name: ")
        discipline_list = self.__controller.filter_disciplines_by_name(name)
        if len(discipline_list) == 0:
            print("No disciplines found under name: ", name)
        else:
            for discipline in discipline_list:
                print(discipline)

    def __add_note(self):
        self.__controller.list_students()
        self.__controller.list_disciplines()
        student_id = input("ID of the student to be noted: ")
        student_id = self.__validator.validate_int(student_id)
        student = self.__controller.repositories.student_repository.find_by_id(student_id)
        if student is None:
            print("No student found under ID: ", student_id)
            return
        else:
            discipline_id = input("ID of the discipline to be updated: ")
            discipline_id = self.__validator.validate_int(discipline_id)
            discipline = self.__controller.repositories.discipline_repository.find_by_id(discipline_id)
            if discipline is None:
                print("No discipline found under ID: ", discipline_id)
                return
            else:
                note = input("Note: ")
                note = self.__validator.validate_note(note)
                self.__note_id_index += 1
                note = Note.Note(student.get_name(), discipline.get_name(), note, self.__note_id_index)
                self.__controller.repositories.note_repository.add(note)

    def __get_notes_ordered_by_student_name_and_discipline(self):
        self.__controller.list_disciplines()
        discipline_id = input("ID of the discipline for the ordering: ")
        discipline_id = self.__validator.validate_int(discipline_id)
        discipline = self.__controller.repositories.discipline_repository.find_by_id(discipline_id)
        if discipline is None:
            print("No discipline found under ID: ", discipline_id)
            return
        else:
            notes = self.__controller.order_notes_by_student_name_and_discipline(discipline.get_name())
            for note in notes:
                print(note)

    def __get_notes_by_note_and_discipline(self):
        self.__controller.list_disciplines()
        discipline_id = input("ID of the discipline for the ordering: ")
        discipline_id = self.__validator.validate_int(discipline_id)
        discipline = self.__controller.repositories.discipline_repository.find_by_id(discipline_id)
        if discipline is None:
            print("No discipline found under ID: ", discipline_id)
            return
        else:
            notes = self.__controller.order_notes_by_note_and_discipline(discipline.get_name())
            for note in notes:
                print(note)

    def __get_best_students(self):
        best_students = self.__controller.get_best_students()
        self.__controller.list_best_students(best_students)
