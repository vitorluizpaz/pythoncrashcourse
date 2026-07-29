magicians = ["David Copperfield", "Harry Houdini", "Dynamo"]


def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)


def make_great(magician_names):
    for index in range(len(magician_names)):
        magician_names[index] = f"{magician_names[index]} the Great"

    return magician_names


great_magicians = make_great(magicians[:])

print("Original magicians:")
show_magicians(magicians)

print("\nGreat magicians:")
show_magicians(great_magicians)