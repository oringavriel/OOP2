from PostFactory import PostFactory


class User:
    _factory = PostFactory()

    # initializes a user
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.log = 1  # user log in when registered
        self.followers = []
        self.post_num = 0
        self.notifications = []
        self.following = []

    # a method that checks if the password that was entered is the correct password of the user
    def is_pass(self, passw):
        if passw != self.password:
            return 0
        return 1

    # follow another user
    def follow(self, other):
        if self.log == 1:
            if other not in self.following:
                self.following.append(other) # adds other user to the user's following list
                other.followers.append(self) # adds the user to the other user's followers list
                print(self.name + " started following " + other.name)

    # unfollow a user
    def unfollow(self, other):
        if self.log == 1:
            if other in self.following:
                self.following.remove(other) # removes the other user from the user's following list
                other.followers.remove(self) # removes the user from the other user's followers list
                print(self.name + " unfollowed " + other.name)

    # publish a new post
    def publish_post(self, post_type, *args):
        if self.log == 1:
            p = self._factory.new_post(post_type, self, *args)
            p.update_all()
            print(p)
            return p

    # adds the notification to the user's notifications list
    def notify(self, note):
        self.notifications.append(note)

    # adds the notification to the user's notifications list and prints it
    def notify_print(self, note_p, note):
        self.notifications.append(note)
        print(note_p)

    def __repr__(self):
        return "User name: {}, Number of posts: {}, Number of followers: {}".format(self.name,
                                                                                    self.post_num, len(self.followers))

    def print(self):
        print(self)

    # prints all user's notifications
    def print_notifications(self):
        print(self.name + "'s notifications:")
        for x in self.notifications:
            print(x)

