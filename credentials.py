import random
import string
import pyperclip
class Credential:
     """
    Class that generates new instances of credentials.
    """

    Credential_list = [] # empty credentials list


    def __init__(self,account,username, password):
        """
        method that defines user credential to be stored
        """
        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self)
        '''
        method that saves credential objects into application
        '''

    def delete_credential(self)
        '''
        method deletes a saved credential from credential_list
        '''

        Credential.Credential_list.remove(self)
