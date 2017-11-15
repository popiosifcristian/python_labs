from repository import Repositories


class Controller:
    def __init__(self) -> None:
        self.repositories = Repositories.Repositories()

    def find_users_by_first_name(self, first_name):
        users = []
        for user in self.repositories.user_repository.get_all():
            if user.get_first_name() == first_name:
                users.append(user)

    def find_users_by_last_name(self, last_name):
        users = []
        for user in self.repositories.user_repository.get_all():
            if user.get_last_name() == last_name:
                users.append(user)
        return users

    @staticmethod
    def __filter_list_by_actor(actor_name, actor_list):
        for name in actor_list:
            if actor_name == name or actor_name in name:
                return True
        return False

    def filter_movies_by_actor(self, actor_name):
        movies = []
        for movie in self.repositories.movie_repository.get_all():
            if self.__filter_list_by_actor(actor_name, movie.get_actor_list()):
                movies.append(movie)
        return movies

    def filter_movies_by_score(self, score):
        movies = []
        for movie in self.repositories.movie_repository.get_all():
            if movie.get_score() > int(score):
                movies.append(movie)
        return movies

    def get_movies_by_ids(self, movie_ids):
        movies = []
        for movie_id in movie_ids:
            movie = self.repositories.movie_repository.find_by_id(movie_id)
            if movie is not None:
                movies.append(movie)
        return movies


class Validator:
    @staticmethod
    def check_int(number):
        """
        This method checks if the received string is a digit.
        :param number: The string to be checked
        :return: True if the received string is a digit, otherwise False.
        """
        if number.isdigit() is False:
            return False
        return True

    @staticmethod
    def check_float(number):
        """
        This method checks if the received string is a float.
        :param number: The string to be checked
        :return: True if the received string is a float, otherwise False.
        """
        try:
            float(number)
        except ValueError:
            return False
        return True

    @staticmethod
    def check_positive(number):
        """
        This method checks if the received number is positive.
        :param number: The number to be checked
        :return: True if the received number is positive, otherwise False.
        """
        if number < 0:
            return False
        return True

    def validate_int(self, number):
        """
        This methods checks if the received string is an int, if its not it will continuous ask for an int.
        :param number: The received string to be checked.
        :return: Received string converted to int.
        """
        while self.check_int(number) is False:
            number = input("Please enter an digit: ")
        return int(number)

    def validate_price(self, price):
        """
        This method will check if the received price is valid, if is not valid, it will loop until
        the user enter a valid price.
        :param price: The price to be checked.
        :return: A valid price.
        """
        while self.check_float(price) is False or self.check_positive(float(price)) is False:
            price = input("Enter a valid price(positive number): ")
        return price

    def validate_score(self, score):
        """
        This method will check if the received score is valid, if is not valid, it will loop until
        the user enter a valid score.
        :param score: The score to be checked.
        :return: A valid score.
        """
        while self.check_float(score) is False or 0 > float(score) or float(score) > 10:
            score = input("Enter a valid score(a number between 0 and 10): ")
        return score

    def validate_year(self, year):
        """
        This method will check if the received year is valid, if is not valid, it will loop until the user enter a valid
        year.
        :param year: The year to be checked.
        :return: A valid year.
        """
        while self.check_int(year) is False or 1000 > int(year) or int(year) > 2017:
            year = input("Please enter a valid year(between 1000 and 2017): ")
        return year
