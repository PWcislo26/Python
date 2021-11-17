from Movie import Movie
import get_movies


def main():
    Movies =[]
    data = get_movies.get_movies()
    for i in range(1, len(data)):
        Movies.append(Movie(data[i][0], data[i][1],data[i][2]).__dict__)
    return Movies









main()