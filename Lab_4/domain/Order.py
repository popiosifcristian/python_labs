class Order:
    def __init__(self, uid, price, movie_list):
        self.__uid = uid
        self.__price = self.__calculate_price(movie_list)
        self.__movie_list = movie_list

    def __str__(self):
        return 'Order{ID: ' + str(self.__uid) + ', Price: ' + str(self.__price) \
               + ', Movies: ' + self.__movie_list + '}'

    def get_uid(self):
        return self.__uid

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
            price += float(movie["price"])
        return price
