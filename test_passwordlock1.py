import unittest
from passwordlock_1 import Credentials

# from passwordlock import User

class TestCredentials(unittest.TestCase):
  '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Twitter","Muriuki","1234yruty")

  def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_name,"Twitter")
        self.assertEqual(self.new_credentials.username,"Muriuki")
        self.assertEqual(self.new_credentials.password,"1234yruty")

  def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the contact list
        '''
        self.new_credentials.save_credentials() 
        self.assertEqual(len(Credentials.credentials_list),1)

  def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

  def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove credentials from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","user","kwekwe") 
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()
            self.assertEqual(len(Credentials.credentials_list),1)

  def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","user","test@user") 
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)

  def test_find_credentials_by_accountname(self):
        '''
        test to check if we can find credentials by account name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","user","test@user")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_accountname("Test")

        self.assertEqual(found_credentials.password,test_credentials.password)

  def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","user","test@user")
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("Test")

        self.assertTrue(credentials_exists)

  def test_display_all_credentials(self):
        '''
        method that returns a list of all credentiasl saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
if __name__ == '__main__':
    unittest.main()