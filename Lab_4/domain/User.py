class User(object):
    """
    User entity class.
    """

    def __init__(self, first_name, last_name, user_id=0):
        """
        The default constructor for the User class.
        :param first_name: First name of the user.
        :param last_name: Last name of the user.
        :param user_id: ID of the user.
        """
        self.__id = user_id
        self.__first_name = first_name.title()
        self.__last_name = last_name.title()

    def __attrs(self):
        """
        This method returns the attributes of this instance of User class.
        :return: ID, first name and last name of this user.
        """
        return self.__id, self.__first_name, self.__last_name

    def __eq__(self, other):
        """
        This method overrides the basic __eq__ methods and verify if the received object is equal to this instance
        of User class.
        :param other: Other object to be verified.
        :return: True if the received object is equal with this user, otherwise False.
        """
        return isinstance(other, User) and self.__attrs() == other.__attrs()

    def __str__(self):
        """
        This method overrides the basic __str__ method and returns a human readable string.
        :return: The string representation of the User class.
        """
        return 'User{ID: ' + str(self.__id) + ', Name: ' + self.__first_name + ' ' + self.__last_name + '}'

    def get_id(self):
        """
        Getter for user id propriety.
        :return: The id of the user.
        """
        return self.__id

    def get_first_name(self):
        """
        Getter for user first name propriety.
        :return: First name of the user.
        """
        return self.__first_name

    def set_first_name(self, new_first_name):
        """
        Setter for user first name propriety.
        :param new_first_name: The new first name to be set.
        """
        self.__first_name = new_first_name

    def get_last_name(self):
        """
        Getter for user last name propriety.
        :return: Last name of the user.
        """
        return self.__last_name

    def set_last_name(self, new_last_name):
        """
        Setter for user last name propriety.
        :param new_last_name: The new last name to be set.
        """
        self.__last_name = new_last_name
