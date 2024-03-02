from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


# factory design pattern
class PostFactory:
    # a method which creates a new post by the post type
    @staticmethod
    def new_post(post_type: str, user, *args):
        if post_type == "Text":
            post = TextPost(user, *args)
            user.post_num += 1
            return post
        elif post_type == "Image":
            post = ImagePost(user, *args)
            user.post_num += 1
            return post
        elif post_type == "Sale":
            post = SalePost(user, *args)
            user.post_num += 1
            return post
        else:
            raise Exception("the type of the post is incorrect")