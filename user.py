class User:
    """
    Class that generates new instances of user
    """

    User_list [] # Empty user list

    def __init__(self,username, password): #method that helps us define properties for our objects.
    
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save new user to the application
        '''
        User.user_list.append(self)

        def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

    @classmethod
    def display_all_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
        