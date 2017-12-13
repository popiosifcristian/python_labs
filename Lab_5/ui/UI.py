import sys
from controller import Controller
from domain import User, Movie, Order


class UI:
    """
    This class contains the UI of the application.
    """

    def __init__(self):
        """
        The default constructor that contains the initialization of the controller and of the validator.
        """
        self.__controller = Controller.Controller()
        self.__validator = Controller.Validator()
        self.__user_id_index = len(self.__controller.repositories.user_repository.get_all())
        self.__movie_id_index = len(self.__controller.repositories.movie_repository.get_all())
        self.__order_id_index = len(self.__controller.repositories.order_repository.get_all())

    __menu_variables = [
        "    ~~~Main Menu~~~ \n"
        "1.User menu \n"
        "2.Movie menu \n"
        "3.Order menu \n"
        "0.Exit \n",

        "    ~~~User Menu~~~ \n"
        "1.Add user \n"
        "2.Update user \n"
        "3.Delete user \n"
        "4.Print users \n"
        "9.Main menu \n"
        "0.Exit \n",

        "    ~~~Movie Menu~~~ \n"
        "1.Add movie \n"
        "2.Update price \n"
        "3.Delete movie \n"
        "4.Print movies \n"
        "9.Main menu \n"
        "0.Exit \n",

        "    ~~~Customer menu~~~ \n"
        "1.Add order \n"
        "2.Print orders \n"
        "3.Filter movies by score \n"
        "4.Filter movies by an actor \n"
        "9.Main menu \n"
        "0.Exit \n",
    ]

    def main_menu(self):
        while True:
            print(self.__menu_variables[0])
            _choice = input("Your choice: ")
            _choice = self.__validator.validate_int(_choice)

            if _choice == 1:
                self.__user_menu()
                break
            elif _choice == 2:
                self.__movie_menu()
                break
            elif _choice == 3:
                self.__customer_menu()
                break
            if _choice == 0:
                self.__controller.update_repositories()
                sys.exit(0)

    def __user_menu(self):
        while True:
            print(self.__menu_variables[1])
            _choice = input("Your choice: ")
            _choice = self.__validator.validate_int(_choice)

            if _choice == 1:
                self.__add_user()
            elif _choice == 2:
                self.__update_user()
            elif _choice == 3:
                self.__delete_user()
            elif _choice == 4:
                self.__print_users()
            elif _choice == 9:
                self.main_menu()
                break
            elif _choice == 0:
                self.__controller.update_repositories()
                sys.exit(0)
            else:
                print("Invalid option.")

    def __movie_menu(self):
        while True:
            print(self.__menu_variables[2])
            _choice = input("Your choice: ")
            _choice = self.__validator.validate_int(_choice)

            if _choice == 1:
                self.__add_movie()
            elif _choice == 2:
                self.__update_movie_price()
            elif _choice == 3:
                self.__delete_movie()
            elif _choice == 4:
                self.__print_movies()
            elif _choice == 9:
                self.main_menu()
                break
            elif _choice == 0:
                self.__controller.update_repositories()
                sys.exit(0)
            else:
                print("Invalid option.")

    def __customer_menu(self):
        while True:
            print(self.__menu_variables[3])
            _choice = input("Your choice: ")
            _choice = self.__validator.validate_int(_choice)

            if _choice == 1:
                self.__add_order()
            elif _choice == 2:
                self.__print_orders()
            elif _choice == 3:
                self.__filter_movies_by_score()
            elif _choice == 4:
                self.__filter_movies_by_actor()
            elif _choice == 9:
                self.main_menu()
                break

            elif _choice == 0:
                self.__controller.update_repositories()
                sys.exit(0)

            else:
                print("Invalid option.")

    def __add_user(self):
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        self.__user_id_index += 1
        user = User.User(first_name, last_name, self.__user_id_index)
        self.__controller.repositories.user_repository.add(user)

    def __update_user(self):
        user_id = input("ID of the user to be updated: ")
        user_id = self.__validator.validate_int(user_id)
        user = self.__controller.repositories.user_repository.find_by_id(user_id)
        if user is not None:
            print(" 1.Edit First Name", '\n', "2.Edit Last Name \n")
            update_choice = input("Your choice: ")
            update_choice = self.__validator.validate_int(update_choice)
            if update_choice == 1:
                first_name = input("Enter new first name: ")
                user.set_first_name(first_name)
                self.__controller.repositories.user_repository.update(user)
            elif update_choice == 2:
                last_name = input("Enter new last name: ")
                user.set_last_name(last_name)
                self.__controller.repositories.user_repository.update(user)
            else:
                print("Invalid option.")
        else:
            print("No user found under ID: ", user_id)

    def __delete_user(self):
        user_id = input("ID of the user to be deleted: ")
        user_id = self.__validator.validate_int(user_id)
        user = self.__controller.repositories.user_repository.find_by_id(user_id)
        if user is not None:
            self.__controller.repositories.user_repository.delete(user)
        else:
            print("No user found under ID: ", user_id)

    def __print_users(self):
        users = self.__controller.repositories.user_repository.get_all()
        for user in users:
            print(user)

    def __add_movie(self):
        title = input("Title: ")
        price = input("Price: ")
        price = self.__validator.validate_price(price)
        score = input("Score: ")
        score = self.__validator.validate_score(score)
        year = input("Apparition year: ")
        year = self.__validator.validate_year(year)
        actors_list = []
        print("How many actors do you want to add in the list?")
        no_of_actors = input("Type your answer here: ")
        no_of_actors = self.__validator.validate_int(no_of_actors)
        for i in range(no_of_actors):
            actor_name = input("Enter a name of an actor: ")
            actors_list.append(actor_name.title())
        self.__movie_id_index += 1
        movie = Movie.Movie(title, price, score, year, actors_list, self.__movie_id_index)
        self.__controller.repositories.movie_repository.add(movie)

    def __delete_movie(self):
        movie_id = input("ID of the movie to be deleted: ")
        movie_id = self.__validator.validate_int(movie_id)
        movie = self.__controller.repositories.movie_repository.find_by_id(movie_id)
        if movie is not None:
            self.__controller.repositories.movie_repository.delete(movie)
        else:
            print("No movie found under ID: ", movie_id)

    def __update_movie_price(self):
        movie_id = input("ID of the movie to be updated: ")
        movie_id = self.__validator.validate_int(movie_id)
        movie = self.__controller.repositories.movie_repository.find_by_id(movie_id)
        if movie is not None:
            price = input("Enter a new price: ")
            price = self.__validator.validate_price(price)
            movie.set_price(price)
            self.__controller.repositories.movie_repository.update(movie)
        else:
            print("No movie found under ID: ", movie_id)

    def __print_movies(self):
        movies = self.__controller.repositories.movie_repository.get_all()
        for movie in movies:
            print(movie)

    def __add_order(self):
        self.__print_users()
        user_id = input("ID of the user for the order: ")
        user_id = self.__validator.validate_int(user_id)
        user = self.__controller.repositories.user_repository.find_by_id(user_id)
        if user is not None:
            movies_ids = []
            self.__print_movies()
            print("How many movies do you want to order?")
            no_of_movies = input("Type your answer here: ")
            no_of_movies = self.__validator.validate_int(no_of_movies)
            for i in range(no_of_movies):
                movie_id = input("Enter the id of the movie: ")
                movie_id = self.__validator.validate_int(movie_id)
                movies_ids.append(movie_id)
            ordered_movies = self.__controller.get_movies_by_ids(movies_ids)
            ordered_movies_titles = self.__controller.get_titles_from_movies(ordered_movies)
            self.__order_id_index += 1
            price = self.__controller.calculate_price(ordered_movies)
            order = Order.Order(user.get_id(), price, ordered_movies_titles, self.__order_id_index)
            self.__controller.repositories.order_repository.add(order)

    def __filter_movies_by_actor(self):
        actor_name = input("Enter the name of the actor for the filter: ")
        actor_name = actor_name.title()
        movies = self.__controller.filter_movies_by_actor(actor_name)
        if movies is None:
            print("No movies with {0}.".format(actor_name))
        else:
            for movie in movies:
                print(movie)

    def __filter_movies_by_score(self):
        score = input("Type the score for the filter: ")
        score = self.__validator.validate_score(score)
        movies = self.__controller.filter_movies_by_score(score)
        if not movies:
            print("No movies with a better score than {0}.".format(score))
        else:
            for movie in movies:
                print(movie)

    def __print_orders(self):
        orders = self.__controller.repositories.order_repository.get_all()
        for order in orders:
            print(order)
