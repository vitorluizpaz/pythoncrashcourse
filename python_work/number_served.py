class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("John's Restaurant", "Brazilian")

# Print the initial number of customers served
print(restaurant.number_served)

# Change the value directly
restaurant.number_served = 20
print(restaurant.number_served)

# Set a new value using the method
restaurant.set_number_served(35)
print(restaurant.number_served)

# Add the number of customers served in one day
restaurant.increment_number_served(15)
print(restaurant.number_served)