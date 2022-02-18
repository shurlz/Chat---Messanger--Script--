### code by John E - Github - Doebaba
# Chat Class
class Chat_App:
    def __init__(self,start=1):
        self.users = {}
        self.logged_in = False # controls user login
        self.current_user = None # keeps track of which user is presently online

    # To enable user registration
    def Sign_Up(self,user_name,password):
        if user_name not in self.users.keys():
            self.users[user_name] = [password,[],{'chatty': 'welcome to the network...'}]  ## password , friends , messages
            return True
        return 'username already taken by another user'

    # enable users log-in
    def log_in(self,username,password):
        if username in self.users.keys() and password == self.users[username][0] and self.logged_in == False:
            self.logged_in = True # automatically dissallows another user from loggin in while there's one online
            self.current_user = username
            messages = self.users[username][2] # collecting all messages
            print(f' login successful {username}!\n Here are your messages :')
            def read_messages():
                for sender in messages.keys():
                    print(f' {sender}: {messages[sender]}') # inner function displaying all messages
            return read_messages()
        if self.logged_in == True:
            return 'Log-in unsuccessful.. Another user still online'
        return 'Invalid log-in credentials' # if the 2 conditions above are False, then log-in credentials are invalid

# function to enable message sending from one user to another
    def send_message(self,reciever_username,message):
        if self.logged_in == True:
            if reciever_username in self.users[self.current_user][1]: # checks for users friends
                self.users[reciever_username][2][self.current_user] = f'{message}'
                return ' Message sent successfully !'
            return f' you have no friend names {reciever_username}'

# adding friends by specific username since the system dissallows registration of tow users by the same username
    def add_friends(self,friend_username):
        if (self.logged_in == True) and (friend_username in self.users.keys()): # checks if a user exists on the system
            self.users[self.current_user][1].append(friend_username)
            return 'Friend added successfully...'

# enables user to successfully log out
    def log_out(self,username):
        if username == self.current_user:
            self.logged_in = False
            return 'logged out successfully'
        return 'logout unsucessful'

# displaying information
    def display_info(self):
        return self.users

user = Chat_App(1)    
