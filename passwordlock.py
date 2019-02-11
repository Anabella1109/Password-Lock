class User:
    '''
    Class that generates new instances of user
    '''
    user_list=[]
    def __init__(self,names,username,email,password):

      '''
      __init__ method that helps define the properties of objects

      Args:
          names:New user full name
          username:New user's username
          email:New user email
          password: New user password

      '''
      self.names=names
      self.username=username
      self.email=email
      self.password=password

    def save_user(self):

         '''
         save_user method saves user objects into user_list
         '''

         User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: Username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns user that matches that username.

        Args:
            username: user to search for
        Returns :
            User that matches that username.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user
    
