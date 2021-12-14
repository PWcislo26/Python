from models.Movie import Movie
from models.Rating import Rating
from models.Tag import Tag
from models.Link import Link
import get_data


def get_movies():
    movies = []
    data = get_data.get_data(r'data/movies.csv')
    for i in range(1, len(data)):
        movies.append(Movie(data[i][0], data[i][1], data[i][2]).__dict__)
    return movies


def get_ratings():
    ratings = []
    data = get_data.get_data(r'data/ratings.csv')
    for i in range(1, len(data)):
        ratings.append(Rating(data[i][0], data[i][1], data[i][2], data[i][3]).__dict__)
    return ratings


def get_tags():
    tags = []
    data = get_data.get_data(r'data/tags.csv')
    for i in range(1, len(data)):
        tags.append(Tag(data[i][0], data[i][1], data[i][2], data[i][3]).__dict__)
    return tags


def get_links():
    links = []
    data = get_data.get_data(r'data/links.csv')
    for i in range(1, len(data)):
        links.append(Link(data[i][0], data[i][1], data[i][2]).__dict__)
    return links
