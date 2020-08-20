from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# config 
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# validating data passed through url
video_put_arg = reqparse.RequestParser()
video_put_arg.add_argument("views", type=int , help="Wrong data! Missing views")
video_put_arg.add_argument("likes", type=int , help="Wrong data! Missing likes")



videos = {
       }


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_arg.parse_args()
        videos[video_id] = args
        return videos[video_id]



# define route 
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)