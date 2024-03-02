from Post import Post


# inherits from post class
class TextPost(Post):

    # initialize a new text post with post abstract class and the text
    def __init__(self, user, text):
        super().__init__(user)
        self._text = text

    def __repr__(self):
        i = '"'
        return "{} published a post:\n{}{}{}\n".format(self._user.name, i, self._text, i)

    def print(self):
        print(self)

