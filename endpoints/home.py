from flask_restful import Resource

class Home(Resource):
    def get(self):
        payload = [
            {
                "Description": "The Thunix API. Please see https://wiki.thunix.net/wiki/api for more information."
            }
        ]

        return payload
