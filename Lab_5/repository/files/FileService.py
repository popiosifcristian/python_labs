from domain import User, Movie, Order


class UserFileService:
    @staticmethod
    def write_users(user_list):
        """
        This method will write in file users from a received list.
        :param user_list: Received list to be written in the file.
        """
        try:
            f = open("users.txt", "w")
            for user in user_list:
                f.write(str(user.get_id()) + ", " + user.get_first_name() + ", " + user.get_last_name() + ", \n")
            f.close()
        except Exception:
            print("Could not save file")

    @staticmethod
    def read_users():
        """
        This method will read users from file.
        :return: A list containing users stored in the file.
        """
        user_list = []
        try:
            f = open("users.txt", "r")
            for line in f.readlines():
                split_line = line.split(", ")
                user_list.append(User.User(split_line[1], split_line[2], split_line[0]))
            f.close()
        except Exception:
            print("Could not read file")
        return user_list


class MovieFileService:
    @staticmethod
    def write_movies(movie_list):
        """
        This method will write in file movies from a received list.
        :param movie_list: Received list to be written in the file.
        """
        try:
            f = open("movies.txt", "w")
            for movie in movie_list:
                f.write(str(movie.get_id()) + ",  " + movie.get_title() + ",  " +
                        str(movie.get_price()) + ",  " + str(movie.get_score()) + ",  " +
                        str(movie.get_year()) + ",  " + str(movie.get_actor_list()) + "\n")
            f.close()
        except Exception:
            print("Could not save file")

    @staticmethod
    def read_movies():
        """
        This method will read movies from file.
        :return: A list containing movies stored in the file.
        """
        movie_list = []
        try:
            f = open("movies.txt", "r")
            for line in f.readlines():
                split_line = line.split(",  ")
                final_actor_list = []
                actor_list = split_line[5]
                actor_list = actor_list[1:-1]
                actor_list = actor_list.split(", ")
                actor_list[-1] = actor_list[-1][0:-1]
                for actor in actor_list:
                    final_actor_list.append(actor[1:-1])
                movie_list.append(Movie.Movie(split_line[1], split_line[2], split_line[3],
                                              split_line[4], final_actor_list, split_line[0]))
            f.close()
        except Exception:
            print("Could not read file")
        return movie_list


class OrderFileService:
    @staticmethod
    def write_orders(order_list):
        """
        This method will write in file orders from a received list.
        :param order_list: Received list to be written in the file.
        """
        try:
            f = open("orders.txt", "w")
            for order in order_list:
                f.write(str(order.get_id()) + ",  " + str(order.get_user_id()) + ",  " +
                        str(order.get_price()) + ",  " + str(order.get_movie_list()) + ",  \n")
            f.close()
        except Exception:
            print("Could not save file")

    @staticmethod
    def read_orders():
        """
        This method will read orders from file.
        :return: A list containing orders stored in the file.
        """
        order_list = []
        try:
            f = open("orders.txt", "r")
            for line in f.readlines():
                split_line = line.split(",  ")
                final_movie_list = []
                movie_list = split_line[3]
                movie_list = movie_list[1:-1]
                movie_list = movie_list.split(", ")
                if len(movie_list) == 1:
                    title = movie_list[-1][1:-1]
                    if title[-1] == "'" or title[-1] == "]":
                        title = title[0:-2]
                        final_movie_list.append(title)
                    else:
                        final_movie_list.append(title)
                else:
                    for movie in movie_list:
                        final_movie_list.append(movie[1:-1])
                order_list.append(Order.Order(split_line[1], split_line[2], final_movie_list, split_line[0]))
            f.close()
        except Exception:
            print("Could not read file")
        return order_list
