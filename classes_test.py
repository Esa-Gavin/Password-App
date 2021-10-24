from classes import User, Credentials  # importing both of my classes
import unittest

class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        '''
        set up method to run before each test cases

        '''
        self.new_user = User("genichiro21", "password")
