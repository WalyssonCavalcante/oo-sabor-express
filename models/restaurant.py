from models.rating import Rating

class Restaurant:
    restaurants = []
    def __init__(self, name, category):
        self._name = name.title()
        self._category = category
        self._active = False
        self._rating = []
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
        rating = Rating(client, note)
        self._rating.append(rating)
    
    @property
    def media_rating(self):
        if not self._rating:
            return 0
        sum_notes = sum(rating._note for rating in self._rating)
        number_notes = len(self._rating)
        average = round(sum_notes / number_notes, 1)
        return average 
