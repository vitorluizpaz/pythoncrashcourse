def make_album(artist_name, album_title):
    cd = {
        "artist_name": artist_name,
        "album_title": album_title
    }

    return cd

while True:
    stop = input("Do you wanna stop? (yes/no)")

    if stop == "yes":
        break

    artist_name = input("Give an artist name: ")
    album_title = input("Give an album title: ")
    make_album(artist_name, album_title)