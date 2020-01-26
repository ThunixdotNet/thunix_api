from flask_restful import Resource
import psutil

class Load(Resource):
    def get(self):
        loadavg = psutil.getloadavg()
        payload = [
            {
                "1min": loadavg[0],
                "5min": loadavg[1],
                "15min": loadavg[2]
            }
        ]
        return payload
