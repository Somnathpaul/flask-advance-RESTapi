from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# config 
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Jk(Resource):
    def get(self):
        return {"data":"hello world"}

# define route 
api.add_resource(Jk, "/jk")

if __name__ == "__main__":
	app.run(debug=True)