# from functionality.functionality import insert_int

"""
This file contains all the functionality for application user management. 
"""

# In memory storage for user management
users = [
    {'id': 0, 'first_name': 'Pop', 'last_name': 'Iosif', 'orders': []},
    {'id': 1, 'first_name': 'Andrei', 'last_name': 'Sipos', 'orders': []},
    {'id': 2, 'first_name': 'Edi', 'last_name': 'Igna', 'orders': []},
    {'id': 3, 'first_name': 'Iluc', 'last_name': 'Paul', 'orders': []},
    {'id': 4, 'first_name': 'Alexandru', 'last_name': 'Sas', 'orders': []},
]
# Unique id for creation of users.
user_id_index = 4


def create_user(first_name, last_name):
    """
    This method will read from the keyboard the required data for creation of an user.
    :return: The user created with the received input data.
    """
    global user_id_index
    user_id_index += 1
    orders = []
    user = {"id": user_id_index, "first_name": first_name.title(), "last_name": last_name.title(), "orders": orders}
    return user


def add_user(user):
    """
    This method will add the received user to the local storage.
    :param user: The received user to be added.
    """
    users.append(user)
    print("The user {0} {1} has been successfully added.".format(user["first_name"], user["last_name"]))


def print_users(l):
    """
    This method will print id and full name of all the users from the received list.
    :param l: The received list to be printed.
    :return: Output data from the received list.
    """
    print("----------------------------------------------")
    for user in l:
        print("ID: {0}, Name: {1} {2}".format(user["id"], user["first_name"], user["last_name"]))
    print("----------------------------------------------")


def find_by_first_name(first_name):
    """
    This method will iterate the local storage and search for all the users that have received first name.
    :return: An user list that contains all the users with the received first name.
    """
    results = []
    for user in users:
        if user["first_name"] == first_name.title():
            results.append(user)
    return results


def find_by_last_name(last_name):
    """
    This method will iterate the local storage and search for all the users that have received last name.
    :return: An user list that contains all the users with the received last name.
    """
    results = []
    for user in users:
        if user["last_name"] == last_name.title():
            results.append(user)
    return results


def find_user_by_id(user_id):
    """
    This method will iterate the local storage and search for the user that have as unique id the received id.
    :param user_id: The unique identifier of users for the search.
    :return: The user that contains the received id, otherwise None.
    """
    for user in users:
        if user["id"] == user_id:
            return user
    print("There is no user with the id: {0}.".format(user_id))
    return None


def delete_user_by_id(user_id):
    """
    This method will delete from the local storage the user that contains the received id if the user exists, otherwise
    prints that it was an unsuccessful deletion.
    :param user_id: The unique identifier for the user that needs to be deleted.
    """
    user = find_user_by_id(user_id)
    if user is None:
        print("Unsuccessful deletion.")
    else:
        users.remove(user)
        print("Successfully deleted user: {0} {1}.".format(user["first_name"], user["last_name"]))


def edit_first_name(user, first_name):
    """
    This method change the first name of the received user.
    :param first_name: The new first name of the user.
    :param user: The user that needs to be edited.
    """
    if user is None:
        print("Unsuccessfully update.")
    else:
        print("Editing user {0} {1}.".format(user["first_name"], user["last_name"]))
        user["first_name"] = first_name.title()
        print("Successfully updated first name of the user.")


def edit_last_name(user, last_name):
    """
    This method change the last name of the received user.
    :param last_name: The new last name of the user.
    :param user: The user that needs to be edited.
    """
    if user is None:
        print("Unsuccessfully update.")
    else:
        print("Editing user {0} {1}.".format(user["first_name"], user["last_name"]))
        user["last_name"] = last_name.title()
        print("Successfully updated first name of the user.")


def add_order_to_user(user, order):
    """
    This method add new order to a user.
    :param user: The user that make the order.
    :param order: The order dictionary with all data about the order.
    """
    user["orders"].append(order)
    print("Successfully added order to user: {0} {1} with value of {2} euros.".format(user["first_name"],
                                                                                      user["last_name"],
                                                                                      order["price"]))


def get_orders(user_list):
    """
    This method gets all the orders from the local storage.
    :param user_list: User lists for orders search.
    :return: All existing orders of users from the received list.
    """
    orders = []
    for user in user_list:
        if user["orders"] is not None:
            for order in user["orders"]:
                orders.append(order)
    return orders


def print_orders(orders):
    """
    This method will print orders in a specific way, naming the user, the price and the movies from the order.
    :param orders: Received orders list to be printed.
    """
    for order in orders:
        movie_list = []
        for movie in order["movies"]:
            movie_list.append(movie["title"])
        print("User: {0}, Price: {1}, Movies: {2}.".format(order["user_id"], order["price"], movie_list))
