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

