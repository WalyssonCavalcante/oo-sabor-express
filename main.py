from models.restaurant import Restaurant

restaurant_park = Restaurant("Brasa & Lenha", 'Churrascaria')
restaurant_mare = Restaurant("Mare Nostrum", "Frutos do Mar")
restaurant_nonna = Restaurant("Nonna Viva", "Italiana")

restaurant_mare.toggle_state()



def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()