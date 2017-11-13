import unittest
from movie.movie import *


class MovieMethodsTests(unittest.TestCase):
    def test_add_movie(self):
        self.assertEqual(len(movies), 2)
        add_movie(create_movie("Title", "100", "5", "2017", actors_list=[]))
        self.assertEqual(len(movies), 3)

    def test_delete_movie(self):
        self.assertEqual(len(movies), 3)
        delete_movie_by_id(len(movies) - 1)
        self.assertEqual(len(movies), 2)

    def test_edit_price(self):
        movie = movies[0]
        old_price = movie["price"]
        new_price = 321
        edit_price(movie, new_price)
        self.assertEqual(movie["price"], new_price)
