class Restaurant:
    restaurants = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._active = False
        Restaurant.restaurants.append(self)
    
    def __str__(self):
        return f'{self.name} | {self.category}'
    
    def list_restaurants():
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurant in Restaurant.restaurants:
            print(f'{restaurant.name.ljust(25)} | {restaurant.category.ljust(25)} | {restaurant.active}')

    @property
    def active(self):
        return 'True ✅' if self._active else 'False ❌'


restaurant_hamburguer = Restaurant('Hamburguer', 'Gourmet')
restaurant_pizza = Restaurant('Pizza', 'Italiana')

Restaurant.list_restaurants()