""" The cart handler """



ab =

class Cart:
    def __init__(self):
        self._cart = dict ()

    def add_item(self, item_name, price):
        if item_name in self._cart:
            price_amount = self._cart[item_name]

        else:
            price_amount = [price, 1]
            self._cart[item_name] = price_amount

