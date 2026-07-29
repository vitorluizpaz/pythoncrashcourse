with open("guest.txt", "a") as file_object:
    while True:
        guest_name = input("What's your name? Type 'quit' to exit: ").strip()

        if guest_name.lower() == "quit":
            break

        print(f"Hello, {guest_name}!")
        file_object.write(f"{guest_name}\n")