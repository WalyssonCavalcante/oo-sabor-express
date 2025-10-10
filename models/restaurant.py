from models.rating import Rating
from models.menu.item_menu import ItemMenu

class Restaurant:
    restaurants = []
    def __init__(self, name, category):
        self._name = name.title()
        self._category = category
        self._active = False
        self._rating = []
        self._menu = []
        Restaurant.restaurants.append(self)
    
    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {'Avaliação'.ljust(25)} | {"Status"}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.media_rating).ljust(25)} | {restaurant.active}')

    @property
    def active(self):
        return 'True ✅' if self._active else 'False ❌'
    
    def toggle_state(self):
        self._active = not self._active

    def receive_rating(self, client, note):
        if 0 < note <= 5:
            rating = Rating(client, note)
            self._rating.append(rating)
    
    @property
    def media_rating(self):
        if not self._rating:
            return '-'
        sum_notes = sum(rating._note for rating in self._rating)
        number_notes = len(self._rating)
        average = round(sum_notes / number_notes, 1)
        return average 
    
    def add_menu(self, item):
        if isinstance(item,ItemMenu):
            self._menu.append(item)
    def show_menu(self):
        print(f'Cardapio do restaurante {self._name}\n')
        for i, item in enumerate(self._menu, start=1):
            if hasattr(item,'description'):
                message_dish = f'{i}. Nome:{item._name} | Preço: R$ {item._price} | Descrição: {item.description}'
                print(message_dish)
            else:
                message_drink = f'{i}. Nome:{item._name} | Preço: R$ {item._price} | Tamanho: {item.size}'
                print(message_drink)