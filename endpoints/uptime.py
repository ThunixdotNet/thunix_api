from flask_restful import Resource
import datetime

class Uptime(Resource):
    def get(self):
        with open("/proc/uptime", "r") as f:
            secs = float(f.readline().split()[0])
        delta = datetime.timedelta(seconds=secs)
    
        payload = [
            {
                "days": delta.days,
                "hours": delta.seconds // 3600,
                "minutes": delta.seconds // 60,
                "seconds": delta.seconds
            }
        ]
    
        return payload
