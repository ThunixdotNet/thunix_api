from flask_restful import Resource

class Teapot(Resource):
    def get(self):
        payload = [
            {
                "tea": "available",
                "height": "short",
                "width": "stout"
            }
        ]
        return payload
