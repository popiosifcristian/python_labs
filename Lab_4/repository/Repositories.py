from repository import AbstractRepository
from domain import User, Movie, Order


class Repositories:
    """
    This class contains all the repositories and the initialization with some objects of the repositories.
    """
    def __init__(self):
        """
        The default constructor of the Repositories class that contains the initialization of repositories and
        stockpiling of some objects.
        """
        self.user_repository = AbstractRepository.AbstractRepository()
        self.movie_repository = AbstractRepository.AbstractRepository()
        self.order_repository = AbstractRepository.AbstractRepository()
        self.initialize_repositories()

    def initialize_repositories(self):
        """
        This method initialize the repositories with some objects.
        """
        movie_1 = Movie.Movie("Pirates Of The Caribbean", 100, 9, 2017,
                              ['Johnny Depp', 'Kevin Mcnally', 'Orlando Bloom'], 1)
        movie_2 = Movie.Movie("Fast & Furious", 90, 8, 2016, ['Vin Diesel', 'Eva Mendes', 'Paul Walker'], 2)
        self.movie_repository.add(movie_1)
        self.movie_repository.add(movie_2)

        user_1 = User.User("Pop", "Iosif", 1)
        user_2 = User.User("Iluc", "Paul", 2)
        self.user_repository.add(user_1)
        self.user_repository.add(user_2)

        order_1 = Order.Order(1, [movie_1], 1)
        order_2 = Order.Order(2, [movie_2], 2)
        self.order_repository.add(order_1)
        self.order_repository.add(order_2)
