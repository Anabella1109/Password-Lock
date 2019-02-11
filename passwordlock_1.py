import random
class Credentials:
     '''
     Class that  generates new instances for acount credentials
     '''
     credentials_list=[]
    #  password_list=[a,,b,c,d,e,f]
     def __init__(self,account_name,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account_name: New account name
            username : New account username
            password: New account password
        '''

        self.account_name=account_name
        self.username=username
        self.password=password


     def save_credentials(self):
          '''
          save_credentials method saves credentials objects into credentials_list
          '''

          Credentials.credentials_list.append(self)

     def delete_credentials(self):

        '''
        delete_credentials method deletes saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    #  def generate_password(self):
    #     '''
    #     generate_password methods generates a random password for the user
    #     '''
        

     @classmethod
     def find_by_accountname(cls,accountname):
        '''
        Method that takes in a name of an account and returns credentials that matches that account name.

        Args:
            accountname: account to search for
        Returns :
            Credentials of person that matches the account name.
        '''

        for account in cls.credentials_list:
            if account.account_name == accountname:
                return account


     @classmethod
     def credentials_exist(cls,accountname):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            number: Account name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exist
        '''
        for account in cls.credentials_list:
            if account.account_name == accountname:
                    return True

        return False

     @classmethod
     def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list