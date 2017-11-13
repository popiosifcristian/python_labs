class User:
    def __init__(self, first_name, last_name, order_ids, uid=0):
        """
        The default constructor for the User class.
        :param uid: User ID.
        :param first_name: First name of the user.
        :param last_name: Last name of the user.
        :param order_ids: A list that contains all the orders ids of this user.
        """
        self.__uid = uid
        self.__first_name = first_name.title()
        self.__last_name = last_name.title()
        self.__order_ids = order_ids

    def __str__(self):
        """
        This method overrides the basic __str__ method and returns a human readable string.
        :return: The string representation of this user class.
        """
        return 'User{ID: ' + str(self.__uid) + ', Name: ' + self.__first_name + ' ' + self.__last_name + '}'

    def get_uid(self):
        return self.__uid

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def get_order_ids(self):
        return self.__order_ids

    def set_order_ids(self, order_ids):
        self.__order_ids = order_ids




u = User("Pop", "Iosif", [])

print(u)

