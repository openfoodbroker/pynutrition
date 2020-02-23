"""Shopping list"""

import pprint


class ShoppingList:
    """Simple shopping list"""

    items = []

    def add(self, items):
        """ Add item to shopping list """
        self.items = self.items + items

    def render(self):
        """print out shopping list"""
        before = len(self.items)
        self.items = list(dict.fromkeys(self.items))
        self.items.sort()
        after = len(self.items)
        for item in self.items:
            print(item)
        print("reduced shopping list from %s to %s" % (before, after))
