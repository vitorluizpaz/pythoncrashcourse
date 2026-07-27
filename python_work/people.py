ana = {"first name": "ana",
    "last name": "beatriz"
    }
vitor = {"first name": "vitor",
         "last name": "paz"
         }
demon1 = {"first name": "nicolas",
          "last name": "karov"}
people = [ana, vitor, demon1]

for person in people:
    print(person["first name"])
    print(f"last name: {person["last name"]}")