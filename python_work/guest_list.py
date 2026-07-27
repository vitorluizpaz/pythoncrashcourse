guests = ["Senna", "Newton", "Einstein"]
message = "Do you want to dinner tonight? Mr "

print(message + guests[0])
print(message + guests[1])
print(message + guests[2])

print(guests[0] + "can't go!")
guests[0] = "Platão"

print(message + guests[0])
print(message + guests[1])
print(message + guests[2])

print("I've found a big dinner table!")
guests.insert(0, "Pelé")
guests.insert(1, "Maradona")
guests.append("Romário")

print("I can only invite two people for dinner!! :(")
guests.pop()
guests.pop()
guests.pop()
guests.pop()

message = "You are still invited Mr. "
print(message + guests[0])
print(message + guests[1])
del guests[0]
del guests[0]

print(guests)