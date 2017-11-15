import unittest
from repository import AbstractRepository


class AbstractRepositoryTests(unittest.TestCase):
    __repository = AbstractRepository.AbstractRepository()

    def test_add_other(self):
        test_object = TestObject("Test Name")
        length = len(self.__repository.get_all())
        self.__repository.add(test_object)
        length += 1
        self.assertEqual(length, len(self.__repository.get_all()))
        self.assertEqual(test_object, self.__repository.find_by_id(test_object.get_id()))

    def test_delete_other(self):
        length = len(self.__repository.get_all())
        length -= 1
        test_object = self.__repository.get_all()[length]
        self.__repository.delete(test_object)
        self.assertEqual(length, len(self.__repository.get_all()))

    def test_update_other(self):
        test_object = TestObject("Test Name")
        self.__repository.add(test_object)
        new_name = "New Test Name"
        test_object.set_name(new_name)
        self.__repository.update(test_object)
        self.assertEqual(new_name, self.__repository.find_by_id(test_object.get_id()).get_name())


class TestObject:
    def __init__(self, name, object_id=0):
        self.__name = name
        self.__id = object_id

    def __str__(self):
        return "TestObject{ID: " + str(self.__id) + ", Name: " + self.__name + "}"

    def __attrs(self):
        return self.__id, self.__name

    def __eq__(self, other):
        return isinstance(other, TestObject) and self.__attrs() == other.__attrs()

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name
