"""
This class contains general functionality for the application.
"""


def check_int(number):
    """
    This method checks if the received string is a digit.
    :param number: The string to be checked
    :return: True if the received string is a digit, otherwise False.
    """
    if number.isdigit() is False:
        return False
    return True


def check_float(number):
    """
    This method checks if the received string is a float.
    :param number: The string to be checked
    :return: True if the received string is a float, otherwise False.
    """
    try:
        float(number)
    except ValueError:
        return False
    return True


def check_positive(number):
    """
    This method checks if the received number is positive.
    :param number: The number to be checked
    :return: True if the received number is positive, otherwise False.
    """
    if number < 0:
        return False
    return True


def validate_int(number):
    """
    This methods checks if the received string is an int, if its not it will continuous ask for an int.
    :param number: The received string to be checked.
    :return: Received string converted to int.
    """
    while check_int(number) is False:
        number = input("Please enter an digit: ")
    return int(number)


def validate_digit(number):
    """
    This methods checks if the received string is an int, if its not it will continuous ask for an int.
    :param number: The received string to be checked.
    :return: Received valid int as a string.
    """
    while check_int(number) is False:
        number = input("Please enter an digit: ")
    return number
