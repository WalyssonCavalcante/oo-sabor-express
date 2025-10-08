class Restaurant:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False

restaurant_hamburguer = Restaurant('Hamburguer', 'Gourmet')
restaurant_pizza = Restaurant('Pizza', 'Italiana')

print (vars(restaurant_hamburguer))
print (vars(restaurant_pizza))
