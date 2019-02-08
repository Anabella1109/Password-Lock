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
        self.new_user = User("James Kaki","Muriuki","james@ms.com","1234yruty") # create user object

  def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.names,"James Kaki")
        self.assertEqual(self.new_user.username,"Muriuki")
        self.assertEqual(self.new_user.email,"james@ms.com")
        self.assertEqual(self.new_user.password,"1234yruty")


if __name__ == '__main__':
    unittest.main()