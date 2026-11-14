def login(username, password):
    if username == "admin" and password == "1234":
        return True
    else:
        return False

import unittest

class TestLogin(unittest.TestCase):

    def test_correct_login(self):
        self.assertTrue(login("admin", "1234"))

    def test_wrong_password(self):
        self.assertFalse(login("admin", "0000"))

    def test_wrong_username(self):
        self.assertFalse(login("user", "1234"))

    def test_empty_username(self):
        self.assertFalse(login("", "1234"))

    def test_empty_password(self):
        self.assertFalse(login("admin", ""))

    def test_both_empty(self):
        self.assertFalse(login("", ""))


unittest.main()