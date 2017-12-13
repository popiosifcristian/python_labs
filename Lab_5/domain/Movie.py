class Movie(object):
    """
    Movie entity class.
    """

    def __init__(self, title, price, score, year, actor_list, movie_id=0):
        """
        The default constructor for the Movie class.
        :param title: Title of the movie.
        :param price: Price of the movie.
        :param score: Score of the movie.
        :param year: Apparition year of the movie.
        :param actor_list: A list of actors that play in this movie.
        :param movie_id: ID of the movie.
        """
        self.__id = int(movie_id)
        self.__title = title
        self.__price = float(price)
        self.__score = float(score)
        self.__year = int(year)
        self.__actor_list = actor_list

    def __attrs(self):
        """
        This method returns the attributes of this instance of Movie class.
        :return: ID, title, price, score, year, actor list.
        """
        return self.__id, self.__title, self.__price, self.__score, self.__year, self.__actor_list

    def __eq__(self, other):
        """
        This method overrides the basic __eq__ methods and verify if the received object is equal to this instance
        of Movie class.
        :param other: Other object to be verified.
        :return: True if the received object is equal with this movie, otherwise False.
        """
        return isinstance(other, Movie) and self.__attrs() == other.__attrs()

    def __str__(self):
        """
        This method overrides the basic __str__ method and returns a human readable string.
        :return: The string representation of the Movie class.
        """
        return 'Movie{ID: ' + str(self.__id) + ', Title: ' + self.__title + ', Price: ' + str(self.__price) \
               + ', Score: ' + str(self.__score) + ', Actors: ' + str(self.__actor_list) + '}'

    def __repr__(self):
        """
        This method overrides the basic __repr__ method and returns a human readable string.
        :return: The string representation of the Movie class.
        """
        return 'Movie{ID: ' + str(self.__id) + ', Title: ' + self.__title + ', Price: ' + str(self.__price) \
               + ', Score: ' + str(self.__score) + ', Actors: ' + str(self.__actor_list) + '}'

    def get_id(self):
        """
        Getter for movie id propriety.
        :return: The id of the movie.
        """
        return self.__id

    def get_title(self):
        """
        Getter for movie title propriety.
        :return: The title of the movie.
        """
        return self.__title

    def set_title(self, title):
        """
        Setter for movie title propriety.
        :param title: The title to be set.
        """
        self.__title = title

    def get_price(self):
        """
        Getter for movie price propriety.
        :return: The price of the movie.
        """
        return self.__price

    def set_price(self, price):
        """
        Setter for movie price propriety.
        :param price: The price to be set.
        """
        self.__price = price

    def get_score(self):
        """
        Getter for movie score propriety.
        :return: The score of the movie.
        """
        return self.__score

    def set_score(self, score):
        """
         Setter for movie score propriety.
         :param score: The score to be set.
         """
        self.__score = score

    def get_year(self):
        """
        Getter for movie year propriety.
        :return: The year of the movie.
        """
        return self.__year

    def set_year(self, year):
        """
         Setter for movie year propriety.
         :param year: The year to be set.
         """
        self.__year = year

    def get_actor_list(self):
        """
        Getter for movie actor list propriety.
        :return: The actor list of the movie.
        """
        return self.__actor_list

    def set_actor_list(self, actor_list):
        """
         Setter for movie actor list propriety.
         :param actor_list: The actor list to be set.
         """
        self.__actor_list = actor_list
