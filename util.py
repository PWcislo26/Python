from models.Movie import Movie
from models.Rating import Rating
import get_data


def get_movies():
    movies = []
    data = get_data.get_data(r'data/movies.csv')
    for i in range(1, len(data)):
        movies.append(Movie(data[i][0], data[i][1],data[i][2]).__dict__)
    return movies

def get_ratings():
    ratings = []
    data = get_data.get_data(r'data/ratings.csv')
    for i in range(1, len(data)):
        ratings.append(Rating(data[i][0], data[i][1], data[i][2], data[i][3]).__dict__)
    return ratings
