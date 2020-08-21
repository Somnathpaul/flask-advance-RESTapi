from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# config 
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# db model 
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes})"

# db.create_all()

# validating data passed through url
video_put_arg = reqparse.RequestParser()
video_put_arg.add_argument("names", type=str, help="Wrong data! Missing name", required=True)
video_put_arg.add_argument("likes", type=int, help="Wrong data! Missing likes", required=True)
video_put_arg.add_argument("views", type=int, help="Wrong data! Missing views", required=True)



videos = {
       }


# if wrong api get called , it will throw an error message with status code
def no_video_id(video_id) :
    if video_id not in videos:
        abort(404, message='Error: Video id not valid')


# if video id already exists then throw an error
def video_id_exists(video_id):
    if video_id in videos:
        abort(400, message="Error: Video id already exists")

class Video(Resource):
    def get(self, video_id):
        # if wrong api called 
        no_video_id(video_id)

        return videos[video_id]

    def post(self, video_id):
        # if video id exists 
        video_id_exists(video_id)

        args = video_put_arg.parse_args()
        videos[video_id] = args
        return videos[video_id]

    def delete(self, video_id):
        # if wrong api called 
        no_video_id(video_id)
        # if exits then delete video id with its data
        del videos[video_id]
        
        return 'Video data deleted', 200




# define route 
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)