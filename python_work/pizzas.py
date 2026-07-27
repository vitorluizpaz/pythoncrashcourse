pizzas = ["Pepperoni", "Margherita", "Four-cheese"]

for pizza in pizzas:
    print(pizza)
    print("I like " + pizza + " pizza.")

print("I like pizza so much!")

print("The first three items in the list are:" + str(pizzas[0:]))
print("The middle item from the list is: " + pizzas[1])
print("The last three items from the list is: " + str(pizzas[-3:]))

friend_pizzas = pizzas[:]
pizzas.append("Calabrese")
friend_pizzas.append("Smoked sausage")

print(pizzas)
print(friend_pizzas)

for pizza in pizzas:
    print(pizza)

for friend_pizza in friend_pizzas:
    print(friend_pizza)