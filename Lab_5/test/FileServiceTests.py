import unittest
from repository.files import FileService
from domain import User, Movie, Order


class FileServiceTests(unittest.TestCase):
    __user_file_service = FileService.UserFileService()
    __movie_file_service = FileService.MovieFileService()
    __order_file_service = FileService.OrderFileService()

    def test_user_file_service(self):
        user_repository = []
        user_1 = User.User("Pop", "Iosif", 1)
        user_2 = User.User("Iluc", "Paul", 2)
        user_repository.append(user_1)
        user_repository.append(user_2)
        self.__user_file_service.write_users(user_repository)
        user_repository_test = self.__user_file_service.read_users()
        working = True
        if len(user_repository) != len(user_repository_test):
            working = False
        for i in range(len(user_repository)):
            if not user_repository[i].__eq__(user_repository_test[i]):
                working = False
        self.assertEqual(True, working)

    def test_movie_file_service(self):
        movie_repository = []
        movie_1 = Movie.Movie("Pirates Of The Caribbean", 100, 9, 2017,
                              ['Johnny Depp', 'Kevin Mcnally', 'Orlando Bloom'], 1)
        movie_2 = Movie.Movie("Fast & Furious", 90, 8, 2016, ['Vin Diesel', 'Eva Mendes', 'Paul Walker'], 2)
        movie_repository.append(movie_1)
        movie_repository.append(movie_2)
        self.__movie_file_service.write_movies(movie_repository)
        movie_repository_test = self.__movie_file_service.read_movies()
        working = True
        if len(movie_repository) != len(movie_repository_test):
            working = False
        for i in range(len(movie_repository)):
            if not movie_repository[i].__eq__(movie_repository_test[i]):
                working = False
        self.assertEqual(True, working)

    def test_order_file_service(self):
        order_repository = []
        movie_1 = Movie.Movie("Pirates Of The Caribbean", 100, 9, 2017,
                              ['Johnny Depp', 'Kevin Mcnally', 'Orlando Bloom'], 1)
        movie_2 = Movie.Movie("Fast & Furious", 90, 8, 2016, ['Vin Diesel', 'Eva Mendes', 'Paul Walker'], 2)
        order_1 = Order.Order(1, 20, [movie_1.get_title()], 1)
        order_2 = Order.Order(2, 30, [movie_2.get_title()], 2)
        order_repository.append(order_1)
        order_repository.append(order_2)
        self.__order_file_service.write_orders(order_repository)
        order_repository_test = self.__order_file_service.read_orders()
        working = True
        if len(order_repository) != len(order_repository_test):
            working = False
        for i in range(len(order_repository)):
            if not order_repository[i].__eq__(order_repository_test[i]):
                working = False
        self.assertEqual(True, working)
