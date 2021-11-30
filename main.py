from flask import Flask
from flask_restful import Resource, Api
from util import get_movies, get_ratings, get_tags, get_links

app = Flask(__name__)
api = Api(app)


class Movies(Resource):
    def get(self):
        return get_movies()


class Ratings(Resource):
    def get(self):
        return get_ratings()


class Tags(Resource):
    def get(self):
        return get_tags()


class Links(Resource):
    def get(self):
        return get_links()


api.add_resource(Movies, '/movies')

api.add_resource(Ratings, '/ratings')

api.add_resource(Tags, '/tags')

api.add_resource(Links, '/links')

if __name__ == '__main__':
    app.run(debug=True)
