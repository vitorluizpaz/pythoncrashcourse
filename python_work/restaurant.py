class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}")
        print(f"Cuisine: {self.cuisine_type}\n")


restaurants = [
    Restaurant("Restaurante do João", "Brazilian"),
    Restaurant("Restaurante do Zeca", "Uruguayan"),
    Restaurant("Restaurante do José", "English"),
]

for restaurant in restaurants:
    restaurant.describe_restaurant()