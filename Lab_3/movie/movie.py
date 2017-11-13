from functionality.functionality import *

"""
This file contains all the functionality for application user management. 

still needs to be done: order and show final price, print orders of users, search movies with score, 
search movies by actor
"""
# In memory storage for movies management
movies = [
    {'id': 0, 'title': 'Pirates Of The Caribbean', 'price': '100', 'score': '4', 'year': '2017',
     'actor_list': ['Johnny Depp', 'Kevin Mcnally', 'Orlando Bloom']},
    {'id': 1, 'title': 'Fast & Furious', 'price': '100', 'score': '9', 'year': '2017',
     'actor_list': ['Vin Diesel', 'Eva Mendes', 'Paul Walker']}
]
# Unique id for creation of movies.
movie_id_index = 1


def create_movie(title, price, score, year, actors_list):
    """
    This method will create the movie dictionary with the received data.
    :return: The movie dictionary created.
    """
    global movie_id_index
    movie_id_index += 1
    movie = {"id": movie_id_index, "title": title.title(), "price": price, "score": score, "year": year,
             "actor_list": actors_list}
    return movie


def validate_price(price):
    """
    This method will check if the received price is valid, if is not valid, it will loop until the user enter a valid
    price.
    :param price: The price to be checked.
    :return: A valid price.
    """
    while check_float(price) is False or check_positive(float(price)) is False:
        price = input("Enter a valid price(positive number): ")
    return price


def validate_score(score):
    """
    This method will check if the received score is valid, if is not valid, it will loop until the user enter a valid
    score.
    :param score: The score to be checked.
    :return: A valid score.
    """
    while check_float(score) is False or 0 > float(score) or float(score) > 10:
        score = input("Enter a valid score(a number between 0 and 10): ")
    return score


def validate_year(year):
    """
    This method will check if the received year is valid, if is not valid, it will loop until the user enter a valid
    year.
    :param year: The year to be checked.
    :return: A valid year.
    """
    while check_int(year) is False or 1000 > int(year) or int(year) > 2017:
        year = input("Please enter a valid year(between 1000 and 2017): ")
    return year


def add_movie(movie):
    """
    This method will add the received movie to the local storage.
    :param movie: The received movie to be added.
    """
    movies.append(movie)
    print("The movie {0} has been successfully added.".format(movie["title"]))


def print_movies(l):
    """
    This method will print id and full name of all the movies from the received list.
    :param l: The received list to be printed.
    :return: Output data from the received list.
    """
    print("----------------------------------------------")
    for movie in l:
        print("ID: {0}, Title: {1}, Price: {2} , Score: {3}".format(movie["id"], movie["title"], movie["price"],
                                                                    movie["score"]))
    print("----------------------------------------------")


def find_movie_by_id(movie_id):
    """
    This method will iterate the local storage and search for the movie that have as unique id the received id.
    :param movie_id: The unique identifier of movies for the search.
    :return: The movie that contains the received id, otherwise None.
    """
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    print("There is no movie with id: {0}.".format(movie_id))
    return None


def delete_movie_by_id(movie_id):
    """
    This method will delete from the local storage the movie that contains the received id if the movie exists,
     otherwise prints that it was an unsuccessful deletion.
    :param movie_id: The unique identifier for the movie that needs to be deleted.
    """
    movie = find_movie_by_id(movie_id)
    if movie is None:
        print("Unsuccessful deletion.")
    else:
        movies.remove(movie)
        print("Successfully deleted movie: {0}.".format(movie["title"]))


def edit_price(movie, price):
    """
    This method edit price of a movie from the local storage if the movie exists,
     otherwise prints that it was an unsuccessful update.
    :param price: The new price for the movie.
    :param movie: The movie that needs to be updated.
    """
    if movie is None:
        print("Unsuccessfully update.")
    else:
        print("Editing price of the movie {0}.".format(movie["title"]))
        movie["price"] = price
        print("Successfully updated price of the movie.")


def get_movies(movies_id):
    """
    This method will receive a list of movie IDs and will return all the movies that exist in our local storage with
    the specific received IDs.
    :param movies_id: A list of IDs.
    :return: A list of movies.
    """
    selected_movies = []
    for mid in movies_id:
        movie = find_movie_by_id(mid)
        if movie is not None:
            selected_movies.append(movie)
    return selected_movies


def create_order(user, order_movies):
    """
    This method will create an order dictionary with the received data.
    :param user: The user that makes the order.
    :param order_movies: The movies selected for the order.
    :return: Order Dictionary.
    """
    order = {"user_id": user["id"], "price": get_price(order_movies), "movies": order_movies}
    return order


def get_price(order_movies):
    """
    This method will sum all the prices from ordered movies.
    :param order_movies: The list of movies from the order.
    :return: The price of all movies from the order.
    """
    price = 0
    for movie in order_movies:
        price += float(movie["price"])
    return price


def filter_by_actor(actor_list, actor_name):
    """
    This method will search in an actor list an actor by name.
    :param actor_list: Actor list for the search.
    :param actor_name: Actor name for the search.
    :return: True if the actor is in that list, otherwise False.
    """
    for actor in actor_list:
        if actor_name == actor or actor_name in actor:
            return True
    return False


def filter_movies_by_actor(movie_list, actor_name):
    """
    This method will filter received movie list by an specific actor name.
    :param movie_list:
    :param actor_name: Received actor name for the filtering.
    :return: All movies that contains in their actor list that specific actor.
    """
    result = []
    for movie in movie_list:
        if filter_by_actor(movie["actor_list"], actor_name) is True:
            result.append(movie)
    return result


def filter_by_score(movie_list, score):
    """
    This method will filter the moves by a specific score.
    :param movie_list: Received list for the filtering.
    :param score: Received score for the filtering.
    :return: All movies that have a better score than the specific score.
    """
    result = []
    for movie in movie_list:
        if float(movie["score"]) > float(score):
            result.append(movie)
    return result
