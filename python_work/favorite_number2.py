import json

number = input("What's your favorite number? ")

with open("favorite_number.json", "w") as f_obj:
    json.dump(number, f_obj)