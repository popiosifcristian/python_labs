class Note(object):
    """
    Note entity class.
    """

    def __init__(self, student_name, discipline_name, note, note_id=0):
        """
        The default constructor for the Note class.
        :param student_name: Name of the student.
        :param discipline_name: Name of the discipline.
        :param note: The note.
        """
        self.__id = note_id
        self.__student_name = student_name
        self.__discipline_name = discipline_name
        self.__note = note

    def __attrs(self):
        """
        This method returns the attributes of this instance of Note class.
        :return: ID, name of the student and name of the discipline.
        """
        return self.__student_name, self.__discipline_name, self.__note

    def __eq__(self, other):
        """
        This method overrides the basic __eq__ methods and verify if the received object is equal to this instance
        of Note class.
        :param other: Other object to be verified.
        :return: True if the received object is equal with this note, otherwise False.
        """
        return isinstance(other, Note) and self.__attrs() == other.__attrs()

    def __str__(self):
        """
        This method overrides the basic __str__ method and returns a human readable string.
        :return: The string representation of the Note class.
        """
        return 'Note{Student: ' + self.__student_name + \
               ', Discipline: ' + self.__discipline_name + \
               ', Note: ' + str(self.__note) + '}'

    def __repr__(self):
        return 'Note{Student: ' + str(self.__student_name) + \
               ', Discipline: ' + str(self.__discipline_name) + \
               ', Note: ' + str(self.__note) + '}'

    def get_id(self):
        """
        Getter for note id propriety.
        :return: The id of the note.
        """
        return self.__id

    def get_student_name(self):
        """
        Getter for student name propriety.
        :return: The name of the student.
        """
        return self.__student_name

    def set_student_name(self, new_name):
        """
        Setter for student name propriety.
        :param new_name: The new name to be set.
        """
        self.__student_name = new_name

    def get_discipline_name(self):
        """
        Getter for discipline name propriety.
        :return: The name of the discipline.
        """
        return self.__discipline_name

    def set_discipline_name(self, new_name):
        """
        Setter for discipline name propriety.
        :param new_name: The new name to be set.
        """
        self.__discipline_name = new_name

    def get_note(self):
        """
        Getter for note propriety.
        :return: The note.
        """
        return self.__note
