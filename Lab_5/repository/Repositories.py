from repository import AbstractRepository
from repository.files import FileService


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
        self.__initialize_repositories()

    def __initialize_repositories(self):
        """
        This method initialize the repositories with some objects.
        """
        users = FileService.UserFileService.read_users()
        movies = FileService.MovieFileService.read_movies()
        orders = FileService.OrderFileService.read_orders()

        for user in users:
            self.user_repository.add(user)
        for movie in movies:
            self.movie_repository.add(movie)
        for order in orders:
            self.order_repository.add(order)

    def update_files(self):
        """
        This method update all files with the local repositories
        """
        FileService.UserFileService.write_users(self.user_repository.get_all())
        FileService.MovieFileService.write_movies(self.movie_repository.get_all())
        FileService.OrderFileService.write_orders(self.order_repository.get_all())
