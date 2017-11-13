# from abc import ABCMeta, abstractmethod
from abc import *


class AbstractRepositoryImpl(ABC):
    """
    This class contains signatures for CRUD methods and generic functionality for repositories.
    """

    __other_list = []

    @classmethod
    def add(cls, other):
        """
        This method will add the received object to the storage.
        :param other: The object to be added.
        """
        cls.__other_list.append(other)
        print(str(other) + " has been added to the repository.")

    @classmethod
    def get_all(cls):
        """
        This method will get all objects from the storage.
        :return: A list with all objects from the storage.
        """
        return cls.__other_list

    @classmethod
    def update(cls, other):
        """
        This method will search for the object in the storage and do the update, otherwise if there is no object in
        the storage will return None.
        :param other: The object to be updated.
        :return: The updated object, otherwise None.
        """
        cls.__other_list[other] = other

    @classmethod
    def delete(cls, other):
        """
        This method will search for the object in the storage, will do the deletion and will return True,
        otherwise if there is no object in the storage will return False.
        :param other: The object to be deleted.
        :return: True if the deletion was done successfully, otherwise False.
        """
        cls.__other_list.remove(other)
        print(other + "has been deleted.")

    @classmethod
    def find_by_id(cls, other_id):
        for other in cls.__other_list:
            if other.id == other_id:
                # print("Found " + other + " under id: " + other_id + ".")
                return other
        return None
