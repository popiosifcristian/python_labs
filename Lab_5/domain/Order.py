class Order(object):
    """
    Order entity class.
    """

    def __init__(self, user_id, price, movie_list, order_id=0):
        """
        The default constructor for the User class.
        :param user_id: User ID that points to the user that made this order.
        :param movie_list: A list of movies that contains all ordered movies.
        :param order_id: ID of the order.
        """
        self.__user_id = int(user_id)
        self.__price = float(price)
        self.__movie_list = movie_list
        self.__id = int(order_id)

    def __attrs(self):
        """
        This method returns the attributes of this instance of Order class.
        :return: ID, user ID, movie list, order id.
        """
        return self.__user_id, self.__price, self.__movie_list, self.__id

    def __eq__(self, other):
        """
        This method overrides the basic __eq__ methods and verify if the received object is equal to this instance
        of Order class.
        :param other: Other object to be verified.
        :return: True if the received object is equal with this movie, otherwise False.
        """
        return isinstance(other, Order) and self.__attrs() == other.__attrs()

    def __str__(self):
        """
        This method overrides the basic __str__ method and returns a human readable string.
        :return: The string representation of the Order class.
        """
        return 'Order{ID: ' + str(self.__id) + ', User ID: ' + str(self.__user_id) + ', Price: ' \
               + str(self.__price) + ', Movies: ' + str(self.__movie_list) + '}'

    def __repr__(self):
        """
        This method overrides the basic __repr__ method and returns a human readable string.
        :return: The string representation of the Order class.
        """
        return 'Order{ID: ' + str(self.__id) + ', User ID: ' + str(self.__user_id) + ', Price: ' \
               + str(self.__price) + ', Movies: ' + str(self.__movie_list) + '}'

    def get_id(self):
        """
        Getter for order id propriety.
        :return: The id of the order.
        """
        return self.__id

    def get_user_id(self):
        """
        Getter for order user id propriety.
        :return: The user id of the order.
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        Setter for order user id propriety.
        :param user_id: The user id to be set.
        """
        self.__user_id = user_id

    def get_price(self):
        """
        Getter for order price propriety.
        :return: The price of the order.
        """
        return self.__price

    def set_price(self, price):
        """
        Setter for order price propriety.
        :param price: The price to be set.
        """
        self.__price = price

    def get_movie_list(self):
        """
        Getter for order movie list propriety.
        :return: The movie list of the order.
        """
        return self.__movie_list

    def set_movie_list(self, movie_list):
        """
        Setter for order movie list propriety.
        :param movie_list: The movie list to be set.
        """
        self.__movie_list = movie_list
