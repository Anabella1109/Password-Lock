#!/usr/bin/env python3.6
from passwordlock import User
from passwordlock_1 import Credentials
import random

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

def main():
  print("Welcome to password locker")
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
      


if __name__ == '__main__':

    main()