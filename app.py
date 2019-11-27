from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from access_fb import get_facebook_status
from access_insta import get_insta_photos
from access_twitter import get_twitter_timeline

app = Flask(__name__)
api = Api(app)

with app.app_context():
    list_items = {"fb":get_facebook_status(), "insta":get_insta_photos(), "twitter" : get_twitter_timeline()}

class Social_Feeds(Resource):
    def get(self):
        return jsonify(list_items)

class Single_Social_Feed(Resource):
    def get(self,sf):
        try:
            return list_items[sf]
        except:
            return jsonify({"error":"invalid option"})

class Index(Resource):
    def get(self):
        content = {"/social_feeds":"to see what's happening in all social networking sites","/social_feeds/input":"for specific social media"}
        return jsonify(content)

api.add_resource(Single_Social_Feed, "/social_feeds/<sf>")
api.add_resource(Social_Feeds, "/social_feeds")
api.add_resource(Index,"/")
app.run(port=5000, debug=True)
