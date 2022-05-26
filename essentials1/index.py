# scraping IMDB  
def get_movies_from_soup(soup):
    movies = []
    for movie in soup.find_all('td', class_='titleColumn'):
        rank = movie.contents[0].text
        title = movie.contents[1].text
        year = movie.contents[2].text
        rating = movie.contents[4].text
        movies.append((rank, title, year, rating))
    return movies


def get_top_bottom_movies(movies):
    top_movies = []
    bottom_movies = []
    for movie in movies:
        if float(movie[3]) > 7.0:
            top_movies.append(movie)
        else:
            bottom_movies.append(movie)
    return top_movies, bottom_movies