import pytest
import unittest
import password_functions


class Fun_test(unittest.TestCase):
    func = password_functions

    def test_check_numbers_for_int(self):
        self.assertIs(self.func.check_numbers_for_int(2, 29), int)

    def test_check_numbers_for_str(self):
        self.assertIs(self.func.check_numbers_for_str(""), str)

    def test_users_name_check(self):
        self.assertFalse(self.func.users_name_check("james", "barton", "password"))

    def test_is_empty(self):
        self.assertIs(self.func.is_empty(""), False)

    def test_DoB_check(self):
        self.assertFalse(self.func.DoB_check("29", "08", "1997", "Password"))

    def test_is_Common(self):
        self.assertFalse(self.func.is_Common("123456789"))
