#!/usr/bin/env python3.6
from passwordlock import User
from passwordlock_1 import Credentials
import random
import string

def create_user(names,username,Email,pw):
    '''
    Function to create new user
    '''
    new_user= User(names,username,Email,pw)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def delet_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a user by a username and return thet user
    '''
    return User.find_by_username(username)

def create_credentials(accountname,username,pw):
    '''
    Function to create new credentials
    '''
    new_credentials=Credentials(accountname,username,pw)
    return new_credentials

def save_credentials(info):
    '''
    Function to save new credentials
    '''
    info.save_credentials()

def delete_creds(info):
    '''
    Function to delete credentials
    '''
    info.delete_credentials()

def find_account(accountname):
    '''
    Function to find credentials by account name
    '''
    return Credentials.find_by_accountname(accountname)

def display():
    '''
      Function to display all saved credentials
    ''' 
    return Credentials.display_credentials()

def check_existing_user(username):
   '''
   Function that checks if user exists with that user name and return a Boolean 
   '''
   return User.user_exist(username)

def check_existing_credentials(accountname):
   '''
   Function that checks if credentials existwith account name and return a Boolean
   '''
   return Credentials.credentials_exist(accountname)

def pw_generator(size,chars=string+ string.digits):
    '''
    Function to generate password for the user
    '''
    return ''.join(random.choice(chars) for _ in range(size))

def main():
  print("Welcome to password locker")

  while True:
    print("\n")
    print("Use the following short codes:ca -Create account ,li -Login")
    short_code1=input().lower()
    if short_code1=='ca':
       print('New account')
       print("-"*10)

       print("Full name")
       names=input()

       print("Login username")
       username=input()

       print("E-mail")
       email=input()

       print("Create password")
       user_password=input()

       save_user(create_user(names,username,email,user_password))
       print('\n')
       print(f"New account {username} created")
       print('\n')
    elif short_code1=='li':
       print("Enter your username")
       login_username=input()

       print("Enter password")
       login_password=input()

       if check_existing_user(login_username):
           search_user=find_user(login_username)
           if search_user.username==login_username and search_user.password==login_password:
             print("Login successful")
             print('\n')
             print("Use the following short codes to navigate your account: ac -add credentials ,fc -find credentials , dc -display credentials,del -delete credentials")
             short_code2=input()
             if short_code2=='ac':
                print("New credentials")
                print("-"*13)

                print("Enter account name/Application name")
                accountname1=input()

                print("Enter username")
                username1=input()

                print("Use cop to create your own password ,gpg to get password generated for you")
                password1=input()

                save_credentials(create_credentials(accountname1,username1,password1))
                print('\n')
                print(f"{accountname1.capitalize()} credentials saved")
                print('\n')
             elif short_code2=='fc':
                print("Enter account name/applicattin name to find")
                accountname=input()

                if check_existing_credentials(accountname):
                  account=find_account(accountname)
                  print('\n')

                  print(f"{accountname.capitalize()}")
                  print("-"*15)

                  print(f"Username ...........{account.username}")
                  print(f"Password..........{account.password}")
                else:
                  print("That account does not exist")

             elif short_code2=='dc':
                 if display():
                    print("Here's a list of all your credentials")
                    print('\n')

                    for credential in display():
                         print(f"{credential.account_name.capitalize()} {credential.username} {credential.password}")
                         print('\n')

                 else:
                    print('\n')
                    print("You don't have any credentials saved yet")
                    print('\n')
             elif short_code2=='del':
                 print("Enter account name you want to delete") 
                 accountname=input()

                 if check_existing_credentials(accountname):
                      account=find_account(accountname)
                      delete_creds(account)
                      print('\n')
                      print(f"{account.account_name}'s credentials are deleted")

                 else:
                   print("\n")
                   print("Account name entered doesn't match any credentials")
                   print('\n')
              

           else :
             print("Wrong username or password")
       else:
           print("Account doesn't exist,You have to create an account first")
       

      


if __name__ == '__main__':

    main()