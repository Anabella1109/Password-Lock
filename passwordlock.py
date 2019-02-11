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
    
