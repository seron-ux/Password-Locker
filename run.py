import getpass
import string

from user import User
from credential import Credential

def create_user(username,password):
    '''
    function to create  new user
    '''
    new_user= User(username,password)
    return new_user
    
def save_user(user):
    '''
    function to save new user
    '''
    User.save_user()
        
def delete_user(user):
    '''
    function that deletes a user
    '''
    User.delete_user() 
        
def find_user(username):
    '''
    function that finds a user
    '''
    return User.find_by_username( username)
    
def check_existing_users(username):
    '''
    function that checks if a user exist
    '''
    return User.user_exist(username)
    
def display_all_users():
    '''
    function that returns all the saved users in the application
    '''
    return User.user.display_all_users()


def create_credential(self, account, username, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential( account, username, password)
    return new_credential


def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()


def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    Credential.credential_list.remove(self)


def find_credential(username):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_credential(username)


def check_existing_credential(username):
    '''
    Function that check if a credential exists with that username and return a Boolean
    '''
    return Credential.credential_exist(username)


def display_credential():
    '''
    Function that returns all the saved credential
    '''
    return Credential.display_credential()


    