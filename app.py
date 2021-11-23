from flask import Flask
from flask_restful import Resource, Api
from util import get_movies, get_ratings


app = Flask(__name__)
api = Api(app)

class Movies(Resource):
    def get(self):
        return get_movies()


class Ratings(Resource):
    def get(self):
        return get_ratings()

api.add_resource(Movies, '/movies')

api.add_resource(Ratings, '/ratings')

if __name__ == '__main__':
    app.run(debug=True)