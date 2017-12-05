class Discipline(object):
    """
    Discipline entity class.
    """

    def __init__(self, name, teacher_name, discipline_id=0):
        """
        The default constructor for the Discipline class.
        :param name: Name of the discipline.
        :param teacher_name: Name of the teacher.
        :param discipline_id: ID of the discipline.
        """
        self.__id = discipline_id
        self.__name = name.title()
        self.__teacher_name = teacher_name.title()

    def __attrs(self):
        """
        This method returns the attributes of this instance of Discipline class.
        :return: ID, name of this discipline.
        """
        return self.__id, self.__name, self.__teacher_name

    def __eq__(self, other):
        """
        This method overrides the basic __eq__ methods and verify if the received object is equal to this instance
        of Discipline class.
        :param other: Other object to be verified.
        :return: True if the received object is equal with this discipline, otherwise False.
        """
        return isinstance(other, Discipline) and self.__attrs() == other.__attrs()

    def __str__(self):
        """
        This method overrides the basic __str__ method and returns a human readable string.
        :return: The string representation of the Discipline class.
        """
        return 'Discipline{ID: ' + str(self.__id) + \
               ', Name: ' + self.__name + ', Teacher Name: ' + self.__teacher_name + '}'

    def get_id(self):
        """
        Getter for discipline id propriety.
        :return: The id of the discipline.
        """
        return self.__id

    def get_name(self):
        """
        Getter for discipline name propriety.
        :return: Name of the discipline.
        """
        return self.__name

    def set_name(self, new_name):
        """
        Setter for discipline name propriety.
        :param new_name: The new name to be set.
        """
        self.__name = new_name

    def get_teacher_name(self):
        """
        Getter for discipline teacher name propriety.
        :return: Teacher name of the discipline.
        """
        return self.__name

    def set_teacher_name(self, new_teacher_name):
        """
        Setter for discipline teacher name propriety.
        :param new_teacher_name: The new name to be set.
        """
        self.__teacher_name = new_teacher_name
