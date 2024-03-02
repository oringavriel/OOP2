from abc import ABC, abstractmethod
from NotifyObserver import NotifyObserver


# abstract class of posts
class Post(ABC):

    _notify_observer = NotifyObserver()

    # initialize a new post
    def __init__(self, user):
        self._user = user
        self._likes = []
        self._comments = []
        self._comments_user = []

    # abstract method which is implemented in child's classes
    @abstractmethod
    def print(self):
        pass

    # notify the user's followers that he posted a new post
    def update_all(self):
        note = self._user.name + " has a new post"
        self._notify_observer.update_followers(self._user, note)

    # likes a post if the user who wants to like is logged in to the social network
    def like(self, other):
        if other.log == 1:
            self._likes.append(other.name)
            if self._user != other:
                note_p = "notification to " + self._user.name + ": " + other.name + " liked your post"
                note = other.name + " liked your post"
                self._notify_observer.update_publisher(self._user, other, note_p, note)

    # comments a post if the user who wants to comment is logged in to the social network
    def comment(self, other, comment):
        if other.log == 1:
            self._comments.append(comment)
            self._comments_user.append(other.name)
            if self._user != other:
                note_p = ("notification to " + self._user.name + ": " + other.name + " commented on your post: " +
                          comment)
                note = other.name + " commented on your post"
                self._notify_observer.update_publisher(self._user, other, note_p, note)
