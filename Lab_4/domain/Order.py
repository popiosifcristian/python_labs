class Order(object):
    def __init__(self, user_id, movie_list, order_id=0):
        self.__user_id = user_id
        self.__price = self.__calculate_price(movie_list)
        self.__movie_list = movie_list
        self.__id = order_id

    def __str__(self):
        return 'Order{ID: ' + str(self.__id) + ', User ID: ' + str(self.__user_id) + ', Movies: ' + str(
            len(self.__movie_list)) + ', Price: ' + str(self.__price) + '}'

    def get_id(self):
        return self.__id

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_movie_list(self):
        return self.__movie_list

    def set_movie_list(self, movie_list):
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
