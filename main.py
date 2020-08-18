from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# config 
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

names = {"python": {"in_use": "true", "version": "3.7"},
        "flask": {"in_sue": "true", "version": "1.1.2"},
        "django": {"in_sue": "false", "version": "none"}
       }


class Jk(Resource):
    def get(self, name):
        return names[name]

# define route 
api.add_resource(Jk, "/jk/<string:name>")

if __name__ == "__main__":
	app.run(debug=True)