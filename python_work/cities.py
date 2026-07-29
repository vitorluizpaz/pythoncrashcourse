cities = {
    "São Paulo": {
        "country": "Brazil",
        "population": 11_500_000,
        "fact": "It is the largest city in Brazil.",
    },
    "New York": {
        "country": "United States",
        "population": 8_300_000,
        "fact": "It is known as the Big Apple.",
    },
    "Tokyo": {
        "country": "Japan",
        "population": 14_000_000,
        "fact": "It is the capital of Japan.",
    },
}

for city, information in cities.items():
    print(f"\nCity: {city}")

    for key, value in information.items():
        print(f"{key.title()}: {value}")