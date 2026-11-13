def search_by_genre(cinema: list, genre: str) -> list:
    return list(filter(lambda x: x['genre']==genre, cinema))

cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]

print(search_by_genre(cinema, input("G: ")))