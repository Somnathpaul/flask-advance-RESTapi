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
video_put_arg.add_argument("likes", type=int, help="Wrong data! Missing likes", required=True)
video_put_arg.add_argument("views", type=int, help="Wrong data! Missing views", required=True)



videos = {
       }


# if wrong api get called , it will throw an error message with status code
def no_video_id(video_id) :
    if video_id not in videos:
        abort(404, message='Error: Video id not valid')




class Video(Resource):
    def get(self, video_id):
        # if wrong api called 
        no_video_id(video_id)
        
        return videos[video_id]

    def post(self, video_id):
        args = video_put_arg.parse_args()
        videos[video_id] = args
        return videos[video_id]



# define route 
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)