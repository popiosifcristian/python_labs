import sys

from user.user import *
from movie.movie import *
from functionality.functionality import *

"""
This file contains all menus for the console application.
"""


def main_menu():
    while True:
        print("......Main Menu......", '\n', "1.User Menu", '\n', "2.Movies Menu", '\n', "3.Customer Menu", '\n',
              "0.Exit")
        choice = input("Your choice: ")
        choice = validate_int(choice)

        if choice == 1:
            user_menu()
            break
        elif choice == 2:
            movie_menu()
            break
        elif choice == 3:
            customer_menu()
            break
        if choice == 0:
            sys.exit(0)


def user_menu():
    while True:
        print("......User Menu......", '\n', "1.Add", '\n', "2.Update", '\n', "3.Delete", '\n', "4.Print Users", '\n',
              "9.Main Menu", '\n', "0.Exit")
        choice = input("Your choice: ")
        choice = validate_int(choice)

        if choice == 1:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            add_user(create_user(first_name, last_name))

        elif choice == 2:
            user_id = input("ID of the user to be updated: ")
            user_id = validate_int(user_id)
            user = find_user_by_id(user_id)
            if user is not None:
                print('\n', "1.Edit First Name", '\n', "2.Edit Last Name")
                update_choice = input("Your choice: ")
                update_choice = validate_int(update_choice)
                if update_choice == 1:
                    first_name = input("Enter new first name: ")
                    edit_first_name(user, first_name)
                elif update_choice == 2:
                    last_name = input("Enter new last name: ")
                    edit_last_name(user, last_name)
                else:
                    print("Invalid option.")

        elif choice == 3:
            user_id = input("ID of the user to be deleted: ")
            user_id = validate_int(user_id)
            delete_user_by_id(user_id)

        elif choice == 4:
            print_users(users)

        elif choice == 9:
            main_menu()
            break

        elif choice == 0:
            sys.exit(0)

        else:
            print("Invalid option.")


def movie_menu():
    while True:
        print("......Movie Menu......", '\n', "1.Add", '\n', "2.Update Price", '\n', "3.Delete", '\n', "4.Print Movies",
              '\n', "9.Main Menu", '\n', "0.Exit")
        choice = input("Your choice: ")
        choice = validate_int(choice)

        if choice == 1:
            title = input("Title: ")
            price = input("Price: ")
            price = validate_price(price)
            score = input("Score: ")
            score = validate_score(score)
            year = input("Apparition year: ")
            year = validate_year(year)
            actors_list = []
            print("How many actors do you want to add in the list?")
            no_of_actors = input("Type your answer here: ")
            no_of_actors = validate_int(no_of_actors)
            for i in range(no_of_actors):
                actor_name = input("Enter a name of an actor: ")
                actors_list.append(actor_name.title())
            add_movie(create_movie(title, price, score, year, actors_list))
        elif choice == 2:
            movie_id = input("ID of the movie to be updated: ")
            movie_id = validate_int(movie_id)
            movie = find_movie_by_id(movie_id)
            price = input("Enter a new price: ")
            price = validate_price(price)
            edit_price(movie, price)
        elif choice == 3:
            print_movies(movies)
            movie_id = input("ID of the movie to be deleted: ")
            movie_id = validate_int(movie_id)
            delete_movie_by_id(movie_id)

        elif choice == 4:
            print_movies(movies)

        elif choice == 9:
            main_menu()
            break

        elif choice == 0:
            sys.exit(0)

        else:
            print("Invalid option.")


def customer_menu():
    while True:
        print("......Customer Menu......", '\n', "1.Place Order", '\n', "2.Print Orders", '\n',
              "3.Filter Movies By Score", '\n', "4.Filter Movies By An Actor", '\n', "9.Main Menu", '\n', "0.Exit")
        choice = input("Your choice: ")
        choice = validate_int(choice)

        if choice == 1:
            user_id = input("ID of the user for the order: ")
            user_id = validate_int(user_id)
            user = find_user_by_id(user_id)
            if user is not None:
                movies_id = []
                print("How many movies do you want to order?")
                no_of_movies = input("Type your answer here: ")
                no_of_movies = validate_int(no_of_movies)
                for i in range(no_of_movies):
                    movie_id = input("Enter the id of the movie: ")
                    movie_id = validate_int(movie_id)
                    movies_id.append(movie_id)
                add_order_to_user(user, create_order(user, get_movies(movies_id)))

        elif choice == 2:
            print_orders(get_orders(users))
        elif choice == 3:
            score = input("Type the score for the filter: ")
            score = validate_score(score)
            result = filter_by_score(movies, score)
            if not result:
                print("No movies with a better score than {0}.".format(score))
            else:
                print_movies(result)
        elif choice == 4:
            actor_name = input("Enter the name of the actor for the filter: ")
            actor_name = actor_name.title()
            result = filter_movies_by_actor(movies, actor_name)
            if result is None:
                print("No movies with {0}.".format(actor_name))
            else:
                print_movies(result)
        elif choice == 9:
            main_menu()
            break

        elif choice == 0:
            sys.exit(0)

        else:
            print("Invalid option.")


main_menu()
