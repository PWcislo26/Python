from flask import Flask
from flask_restful import Resource, Api
from main import main

data = main()

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return data

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)