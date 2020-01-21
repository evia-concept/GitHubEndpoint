from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


class Contributors(Resource):
    def get(self, org_name):

        return "Not yet implemented", 404

    def post(self, org_name):

        return "Method not allowed", 405

    def put(self, org_name):

        return "Method not allowed", 405

    def delete(self, org_name):

        return "Method not allowed", 405


api.add_resource(Contributors, "/<string:org_name>/contributors")

app.run(port=8080, debug=True)
