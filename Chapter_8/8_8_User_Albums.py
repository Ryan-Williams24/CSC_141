def make_album(artist, title):
    album = {"artist": artist, "title": title}
    return album

while True:
    artist = input("Enter the artist's name (or 'quit' to exit): ")
    if artist == 'quit':
        break
    title = input("Enter the album title: ")
    album = make_album(artist, title)
    print(album)