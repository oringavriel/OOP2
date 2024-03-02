from User import User


# singleton design pattern
class SocialNetwork:
    # initializing the social network instance as none
    __instance = None

    # returns the social network instance if exists. the method gives global access to the instance
    @staticmethod
    def get_instance():
        if SocialNetwork.__instance is not None:
            return SocialNetwork.__instance

    # if the instance was yet created , the method creates a new sole instance and returns it
    def __new__(cls, net_name):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    # initializes the social network with name and a list of users registered
    def __init__(self, net_name):
        self._netName = net_name
        self._usersList = []
        print("The social network", self._netName, "was created!")

    # checks if the desired username is available
    def check_name(self ,username):
        for x in self._usersList:
            if username == x.name:
                return 0
        return 1

    '''
    the method signs a new user to the social network . 
    it checks if the password is between 4-8 digits and if the username is available.
    if so, it creates a new user and adds it to the users 
    '''
    def sign_up(self, username, password):
        if self.check_name(username) == 0:
            raise Exception("choose a different username")
        if len(password) > 8 or len(password) < 4:
            raise Exception("enter a password with 4-8 digits")
        else:
            u = User(username, password)
            self._usersList.append(u)
            return u

    # the method allows the user to log in by entering the correct username and password
    def log_in(self, name, password):
        for x in self._usersList:
            if x.name == name and x.is_pass(password) == 1:
                x.log = 1
                print(name, "connected")

    # the method allows the user to log out of the network
    def log_out(self, name):
        for x in self._usersList:
            if x.name == name:
                x.log = 0
                print(name, "disconnected")

    # returns the social network data as a string
    def __repr__(self):
        st = "\n".join([str(i) for i in self._usersList])
        return "{} social network:\n{}".format(self._netName, st)

    # prints the social network data
    def print(self):
        print(self)

