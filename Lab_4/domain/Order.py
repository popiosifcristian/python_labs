class Order(object):
    """
    Order entity class.
    """

    def __init__(self, user_id, movie_list, order_id=0):
        """
        The default constructor for the User class.
        :param user_id: User ID that points to the user that made this order.
        :param movie_list: A list of movies that contains all ordered movies.
        :param order_id: ID of the order.
        """
        self.__user_id = user_id
        self.__price = self.__calculate_price(movie_list)
        self.__movie_list = movie_list
        self.__id = order_id

    def __str__(self):
        """
        This method overrides the basic __str__ method and returns a human readable string.
        :return: The string representation of the Order class.
        """
        return 'Order{ID: ' + str(self.__id) + ', User ID: ' + str(self.__user_id) + ', Movies: ' + str(
            len(self.__movie_list)) + ', Price: ' + str(self.__price) + '}'

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

    @staticmethod
    def __calculate_price(movies):
        """
        This method will sum all the prices from ordered movies.
        :param movies: The list of movies from the order.
        :return: The price of all movies from the order.
        """
        price = 0
        for movie in movies:
            price += float(movie.get_price())
        return price
