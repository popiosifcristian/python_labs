import unittest
from controller import Controller


class ControllerTests(unittest.TestCase):
    __controller = Controller.Controller()

    def test_find_users_by_first_name(self):
        length = len(self.__controller.repositories.user_repository.get_all())
        test_user = self.__controller.repositories.user_repository.get_all()[length - 1]
        users = self.__controller.find_users_by_first_name(test_user.get_first_name())
        found = False
        for user in users:
            if user.__eq__(test_user):
                found = True
        self.assertEqual(True, found)

    def test_find_users_by_first_name_none_first_name(self):
        users = self.__controller.find_users_by_first_name(None)
        self.assertEqual(0, len(users))

    def test_find_users_by_last_name(self):
        length = len(self.__controller.repositories.user_repository.get_all())
        test_user = self.__controller.repositories.user_repository.get_all()[length - 1]
        users = self.__controller.find_users_by_last_name(test_user.get_last_name())
        found = False
        for user in users:
            if user.__eq__(test_user):
                found = True
        self.assertEqual(True, found)

    def test_find_users_by_last_name_none_first_name(self):
        users = self.__controller.find_users_by_last_name(None)
        self.assertEqual(0, len(users))

    def test_filter_movies_by_actor(self):
        length = len(self.__controller.repositories.movie_repository.get_all())
        test_movie = self.__controller.repositories.movie_repository.get_all()[length - 1]
        actor_list_length = len(test_movie.get_actor_list())
        actor_name = test_movie.get_actor_list()[actor_list_length - 1]
        movies = self.__controller.filter_movies_by_actor(actor_name)
        found = False
        for movie in movies:
            if movie.__eq__(test_movie):
                found = True
        self.assertEqual(True, found)

    def test_filter_movies_by_actor_none_actor(self):
        movies = self.__controller.filter_movies_by_actor(None)
        self.assertEqual(0, len(movies))

    def test_filter_movies_by_score(self):
        length = len(self.__controller.repositories.movie_repository.get_all())
        test_movie = self.__controller.repositories.movie_repository.get_all()[length - 1]
        score = test_movie.get_score()
        score -= 1
        movies = self.__controller.filter_movies_by_score(score)
        found = False
        for movie in movies:
            if movie.__eq__(test_movie):
                found = True
        self.assertEqual(True, found)

    def test_filter_movies_by_score_0(self):
        length = len(self.__controller.repositories.movie_repository.get_all())
        score = 0
        movies = self.__controller.filter_movies_by_score(score)
        self.assertEqual(length, len(movies))

    def test_filter_movies_by_score_none_score(self):
        movies = self.__controller.filter_movies_by_actor(None)
        self.assertEqual(0, len(movies))

    def test_get_movies_by_ids(self):
        length = len(self.__controller.repositories.movie_repository.get_all())
        test_movie = self.__controller.repositories.movie_repository.get_all()[length - 1]
        movies_ids = [test_movie.get_id()]
        movies = self.__controller.get_movies_by_ids(movies_ids)
        self.assertEqual(test_movie, movies[0])
