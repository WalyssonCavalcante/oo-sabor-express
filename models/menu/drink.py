from models.menu.item_menu import ItemMenu

class Drink(ItemMenu  ):
    def __init__(self,name, price, size ):
        super().__init__(name,price)
        self.size = size

    def __str__(self):
        return self._name
    
    def apply_discount(self):
        self._preco -= (self._preco * 0.08)