from flask_restful import Resource, abort

class Disk(Resource):
    def get(self):
        abort(501, message="Not currently implemented.")
