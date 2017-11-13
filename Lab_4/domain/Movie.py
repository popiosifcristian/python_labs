class Movie:
    def __init__(self, title, price, score, year, actor_list, mid=0):
        self.__mid = mid
        self.__title = title
        self.__price = price
        self.__score = score
        self.__year = year
        self.__actor_list = actor_list

    def __str__(self):
        return 'Movie{ID: ' + str(self.mid) + ', Title: ' + self.title + ', Price: ' + str(self.price) \
               + ', Score: ' + str(self.score) + '}'

    def get_mid(self):
        return self.__mid

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
