from classes import User, Credentials  # importing both of my classes
import unittest

class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        '''
        set up method to run before each test cases

        '''
        self.new_user = User("genichiro21", "password")

    def test_init(self):
        '''
        test to check whether the class has been initialized

        '''
        self.assertEqual(self.new_user.username, "genichiro21")
        self.assertEqual(self.new_user.password, "password")
