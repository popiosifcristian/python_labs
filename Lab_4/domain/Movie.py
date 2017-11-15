class Movie(object):
    def __init__(self, title, price, score, year, actor_list, movie_id=0):
        self.__id = movie_id
        self.__title = title
        self.__price = price
        self.__score = score
        self.__year = year
        self.__actor_list = actor_list

    def __str__(self):
        return 'Movie{ID: ' + str(self.__id) + ', Title: ' + self.__title + ', Price: ' + str(self.__price) \
               + ', Score: ' + str(self.__score) + '}'

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_actor_list(self):
        return self.__actor_list

    def set_actor_list(self, actor_list):
        self.__actor_list = actor_list
