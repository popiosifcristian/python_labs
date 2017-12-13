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

    def test_add_two_other(self):
        test_object_1 = TestObject("Test Name 1", 1)
        test_object_2 = TestObject("Test Name 2", 2)
        length = len(self.__repository.get_all())
        self.__repository.add(test_object_1)
        self.__repository.add(test_object_2)
        length += 2
        self.assertEqual(length, len(self.__repository.get_all()))
        self.assertEqual(test_object_1, self.__repository.find_by_id(test_object_1.get_id()))
        self.assertEqual(test_object_2, self.__repository.find_by_id(test_object_2.get_id()))

    def test_add_three_other(self):
        test_object_1 = TestObject("Test Name 1", 1)
        test_object_2 = TestObject("Test Name 2", 2)
        test_object_3 = TestObject("Test Name 3", 3)
        length = len(self.__repository.get_all())
        self.__repository.add(test_object_1)
        self.__repository.add(test_object_2)
        self.__repository.add(test_object_3)
        length += 3
        self.assertEqual(length, len(self.__repository.get_all()))
        self.assertEqual(test_object_1, self.__repository.find_by_id(test_object_1.get_id()))
        self.assertEqual(test_object_2, self.__repository.find_by_id(test_object_2.get_id()))
        self.assertEqual(test_object_3, self.__repository.find_by_id(test_object_3.get_id()))

    def test_add_none__delete__none(self):
        test_object = None
        length = len(self.__repository.get_all())
        self.__repository.add(test_object)
        length += 1
        self.assertEqual(length, len(self.__repository.get_all()))
        self.assertEqual(test_object, self.__repository.get_all()[length - 1])
        self.__repository.delete(self.__repository.get_all()[length - 1])

    def test_delete_other(self):
        test_object = TestObject("Test Name")
        self.__repository.add(test_object)
        length = len(self.__repository.get_all())
        length -= 1
        test_object = self.__repository.get_all()[length]
        self.__repository.delete(test_object)
        self.assertEqual(length, len(self.__repository.get_all()))

    def test_delete_all(self):
        length = len(self.__repository.get_all())
        while length > 0:
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

    def test_update_other_1(self):
        test_object = TestObject("Test Name")
        self.__repository.add(test_object)
        new_name = "New Name"
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
