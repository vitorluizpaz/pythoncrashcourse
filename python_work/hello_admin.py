usernames = ["basic", "erde", "kprix", "demon1", "art", "admin"]


if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello boss!")
        else:
            print(f"Hello {username}")
else:
    print("We need to find some users!")