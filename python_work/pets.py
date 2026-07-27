amora = {"type": "cat",
    "owner": "rubia"}
sophi = {"type": "cat",
    "owner": "vitor"}
orion = {"type": "dog",
    "owner": "vitor"}

pets = [amora, sophi, orion]

for pet in pets:
    print(f"Type: {pet["type"]}")
    print(f"Owner: {pet["owner"]}")
