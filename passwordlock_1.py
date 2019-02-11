class Credentials:
     '''
     Class that  generates new instances for acount credentials
     '''
     credentials_list=[]
     def __init__(self,account_name,username,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account_name: New account name
            username : New account username
            password: New account password
        '''

        self.account_name:account_name
        self.username:username
        self.password:password


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