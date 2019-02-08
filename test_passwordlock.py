import unittest
from passwordlock import User
from passwordlock_1 import Credentials

class TestUser(unittest.TestCase):
  '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James Kaki","Muriuki","james@ms.com","1234yruty") # create contact object