class AbstractRepository(object):
    """
    This class contains signatures for CRUD methods and generic functionality for repositories.
    """

    def __init__(self):
        """
        The default constructor for the AbstractRepository class.
        """
        self.__other_list = []

    def add(self, other):
        """
        This method will add the received object to the storage.
        :param other: The object to be added.
        """
        self.__other_list.append(other)
        print(str(other) + " has been added to the repository.")

    def get_all(self):
        """
        This method will get all objects from the storage.
        :return: A list with all objects from the storage.
        """
        return self.__other_list

    def update(self, other):
        """
        This method will search for the object in the storage and will do the update if there is any object with same
        id in repository.
        :param other: The object to be updated.
        """
        position = 0
        for item in self.__other_list:
            if item.get_id == other.get_id:
                break
            position += 1
        self.__other_list[position] = other

    def delete(self, other):
        """
        This method will search for the object in the storage, will do the deletion and return True,
        otherwise if there is no object matching the received object in the storage will return False.
        :param other: The object that needs to be deleted.
        :return: True if the deletion was done successfully, otherwise False.
        """
        self.__other_list.remove(other)
        print("{0} has been deleted.".format(other))

    def find_by_id(self, other_id):
        """
        This method will search in the repository for any object that contains same ID as received ID.
        :param other_id: The received ID for the search.
        :return: Found object if there is any, otherwise None.
        """
        for other in self.__other_list:
            if other.get_id() == other_id:
                return other
        return None
