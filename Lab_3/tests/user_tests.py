import unittest
from user.user import *


class UserMethodsTests(unittest.TestCase):
    def test_add_user(self):
        self.assertEqual(len(users), 5)
        users.append(create_user("Test", "Test"))
        self.assertEqual(len(users), 6)

    # def test_find_by_first_name(self):
    #     first_name = "Pop"
    #     test_results = find_by_first_name(first_name)
    #     test = True
    #     for user in test_results:
