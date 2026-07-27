favorite_places = {
    "vitor": ["Hawaii", "New York", "Lisbon"],
    "maria": ["Paris", "Rome"],
    "lucas": ["Tokyo"]
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")

    for place in places:
        print(f"- {place}")