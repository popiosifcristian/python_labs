from repository import AbstractRepository
from domain import User, Movie, Order


class Repositories:
    def __init__(self):
        self.user_repository = AbstractRepository.AbstractRepositoryImpl()
        self.movie_repository = AbstractRepository.AbstractRepositoryImpl()
        self.order_repository = AbstractRepository.AbstractRepositoryImpl()
        self.initialize_repositories()

    def initialize_repositories(self):
        movie_1 = Movie.Movie("Pirates Of The Caribbean", 100, 9, 2017,
                              ['Johnny Depp', 'Kevin Mcnally', 'Orlando Bloom'])
        movie_2 = Movie.Movie("Fast & Furious", 90, 8, 2016, ['Vin Diesel', 'Eva Mendes', 'Paul Walker'])
        self.movie_repository.add(movie_1)
        self.movie_repository.add(movie_2)


movie_2 = Movie.Movie("Fast & Furious", 90, 8, 2016, ['Vin Diesel', 'Eva Mendes', 'Paul Walker'])
print(movie_2)
