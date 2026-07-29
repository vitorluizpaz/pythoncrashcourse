toppings = []

message = ""

while message != "quit":
    message = input("Enter a topping or 'quit': ")

    if message != "quit":
        toppings.append(message)

print(toppings)