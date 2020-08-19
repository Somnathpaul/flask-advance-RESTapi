from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# config 
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

video_put_arg = reqparse.RequestParser()
video_put_arg.add_argument("name", type=str , help={"Wrong data! Missing name."})
video_put_arg.add_argument("views", type=int , help={"Wrong data! Missing views."})
video_put_arg.add_argument("likes", type=int , help={"Wrong data! Missing likes."})
video_put_arg.add_argument("dislikes", type=int , help={"Wrong data! Missing dislikes."})



videos = {
       }


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        print(request.form['likes'])
        return {"ok": "21"}



# define route 
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)