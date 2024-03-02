from Post import Post


# inherits from post class
class SalePost(Post):
    
    # initialize a new sale post with post abstract class and item details 
    def __init__(self, user, item, price, place):
        super().__init__(user)
        self._item = item
        self._price = price
        self._place = place
        self._available = 1  # when first posted the item is available

    def __repr__(self):
        if self._available == 0:
            return ("{} posted a product for sale:\nSold! {}, price: {}, pickup from: {}\n".format(self._user.name,
                                                                                                   self._item,
                                                                                                   self._price,
                                                                                                   self._place))
        return "{} posted a product for sale:\nFor sale! {}, price: {}, pickup from: {}\n".format(self._user.name,
                                                                                                  self._item,
                                                                                                  self._price,
                                                                                                  self._place)

    # by entering the password the user can change the item from available to sold 
    def sold(self, password):
        if self._user.is_pass(password) == 1:
            self._available = 0
            note = self._user.name + "'s product is sold"
            print(self._user.name + "'s product is sold")
            self._user.notifications.append(note)

    # by entering the password the user enter a discount on the product
    def discount(self, percent, password):
        if self._user.is_pass(password) == 1:
            self._price = self._price - ((self._price * percent) / 100) # discount calculate
            note = "Discount on " + self._user.name + " product! the new price is:", self._price
            print("Discount on " + self._user.name + " product! the new price is:", self._price)
            self._user.notifications.append(note)

    def print(self):
        print(self)
