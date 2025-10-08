class Restaurant:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
    
    def __str__(self):
        return f'{self.name} | {self.category}'

restaurant_hamburguer = Restaurant('Hamburguer', 'Gourmet')
restaurant_pizza = Restaurant('Pizza', 'Italiana')

print (restaurant_hamburguer)
print (restaurant_pizza)
