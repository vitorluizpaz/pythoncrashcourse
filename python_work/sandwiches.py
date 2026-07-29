def make_sandwich(*toppings):
    print("\nYour sandwich contains:")

    for topping in toppings:
        print(f"- {topping}")


make_sandwich("cheese")
make_sandwich("ham", "cheese")
make_sandwich("chicken", "lettuce", "tomato", "mayonnaise")