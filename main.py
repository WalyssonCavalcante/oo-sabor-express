from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish

restaurant_park = Restaurant("Brasa & Lenha", 'Churrascaria')
restaurant_mare = Restaurant("Mare Nostrum", "Frutos do Mar")
restaurant_nonna = Restaurant("Nonna Viva", "Italiana")
drink_juice = Drink("Suco de Goiaba", 5.0, 'grande')
drink_juice.apply_discount()
dish_bread = Dish("Pão", 2.00, 'O melhor pão da cidade')
dish_bread.apply_discount()
restaurant_park.add_menu(dish_bread)
restaurant_park.add_menu(drink_juice)

def main():
    restaurant_park.show_menu()
    

if __name__ == '__main__':
    main()