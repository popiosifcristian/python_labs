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
            if movie.get_score() > score:
                movies.append(movie)
        return movies

    
