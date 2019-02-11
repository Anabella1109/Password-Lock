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

  def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the contact list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)

  def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

  def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","test@user.com","kwekwe") 
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()