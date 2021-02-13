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