class Student(object):
    """
    Student entity class.
    """

    def __init__(self, name, student_id=0):
        """
        The default constructor for the Student class.
        :param name: Name of the student.
        :param student_id: ID of the student.
        """
        self.__id = student_id
        self.__name = name.title()

    def __attrs(self):
        """
        This method returns the attributes of this instance of Student class.
        :return: ID, name of this student.
        """
        return self.__id, self.__name

    def __eq__(self, other):
        """
        This method overrides the basic __eq__ methods and verify if the received object is equal to this instance
        of Student class.
        :param other: Other object to be verified.
        :return: True if the received object is equal with this student, otherwise False.
        """
        return isinstance(other, Student) and self.__attrs() == other.__attrs()

    def __str__(self):
        """
        This method overrides the basic __str__ method and returns a human readable string.
        :return: The string representation of the Student class.
        """
        return 'Student{ID: ' + str(self.__id) + ', Name: ' + self.__name + '}'

    def get_id(self):
        """
        Getter for student id propriety.
        :return: The id of the student.
        """
        return self.__id

    def get_name(self):
        """
        Getter for student name propriety.
        :return: Name of the student.
        """
        return self.__name

    def set_name(self, new_name):
        """
        Setter for student name propriety.
        :param new_name: The new name to be set.
        """
        self.__name = new_name
