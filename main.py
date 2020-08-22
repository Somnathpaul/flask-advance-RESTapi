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

# post : validating data passed through url
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Wrong data! Missing name", required=True)
video_put_args.add_argument("likes", type=int, help="Wrong data! Missing likes", required=True)
video_put_args.add_argument("views", type=int, help="Wrong data! Missing views", required=True)

# patch : validating data passed through url
video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument("name", type=str, help="Wrong data! Missing name")
video_patch_args.add_argument("likes", type=int, help="Wrong data! Missing name")
video_patch_args.add_argument("views", type=int, help="Wrong data! Missing name")




# how the function will throw out the data 
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.String,
    'likes': fields.String
}

# working without database
#videos = {}




class Video(Resource):
    # resource fields called so that it returns json format
    @marshal_with(resource_fields)
    def get(self, video_id):
        # get video details through id 
        result = VideoModel.query.filter_by(id = video_id).first()
        # if video not found
        if result is None :
            abort(404, message = 'Error: Video not found')
        return result


    # resource fields called so that it returns json format
    @marshal_with(resource_fields)
    def post(self, video_id):
        # resource fields called so that it returns json format
        args = video_put_args.parse_args()
        # check if the video is already taken or not
        result = VideoModel.query.filter_by(id=video_id).first()
        # if taken throw error
        if result:
            abort(409, message = 'Error: Video id already taken')
        
        # save the data
        video_data = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video_data)
        db.session.commit()
        return video_data

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        if result: 
            db.session.delete(result)
            db.session.commit()
            return 'Video deleted'
        
        abort(204, message = 'Error: Video id not available')

    # resource fields called so that it returns json format
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_patch_args.parse_args()
        # check if the video is present or not
        result = VideoModel.query.filter_by(id=video_id).first()
        
        # if result found 
        if result :
            if args['name']:
                result.name = args['name']
            if args['views']:
                result.views = args['views']
            if args['likes']:
                result.likes = args['likes']
            db.session.commit()
            return result
        abort(204, message='Error: Video id not found') 



# define route 
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True)