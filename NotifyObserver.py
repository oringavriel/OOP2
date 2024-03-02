# observer design pattern implemented in notifications
class NotifyObserver:

    # notify the user about his personal notifications
    @staticmethod
    def update_publisher(publisher, observer, note_p, note):
        if publisher != observer:
            publisher.notify_print(note_p, note)

    # notify all the user's followers he uploaded a post
    @staticmethod
    def update_followers(observer, note):
        for x in observer.followers:
            x.notify(note)
