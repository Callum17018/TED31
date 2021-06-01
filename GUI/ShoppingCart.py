""" The cart handler """


class Cart:
    def __init__(self):
        """ Creates an empty cart """
        self._cart = dict ()

    def add_item(self, item_name, price):
        """ Adds items to the cart """
        if item_name in self._cart:
            price_amount = self._cart[item_name]
            price, amount = price_amount
            amount += 1
            price_amount = [price, amount]
            self._cart[item_name] = price_amount

        else:
            price_amount = [price, 1]
            self._cart[item_name] = price_amount

    def get_items(self):
        """ Returns a list of all items, prices and amounts """
        return self._cart

    def get_total_cost(self):
        """ Returns the total cost of the cart """
        total = 0
        cart = self.get_items()
        for item in cart:
            price, amount = cart[item]
            total += (price * amount)

        return total

