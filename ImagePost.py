import matplotlib.pyplot as plt
from Post import Post
from PIL import Image


# inherits from post class
class ImagePost(Post):
    # initialize a new image post with post abstract class and image path
    def __init__(self, user, image):
        super().__init__(user)
        self._image = image

    def __repr__(self):
        return "{} posted a picture\n".format(self._user.name)

    # displays the image
    def display(self):
        print("Shows picture")
        img = Image.open(self._image)
        plt.imshow(img)
        plt.show()

    def print(self):
        print(self)
