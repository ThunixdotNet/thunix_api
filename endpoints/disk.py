from flask_restful import Resource, abort
import psutil

class Disk(Resource):
    def get(self):
        disk_usage = psutil.disk_usage('/')
        payload = {
            "total":disk_usage.total,
            "used":disk_usage.used,
            "percentused":disk_usage.percent
            }
        return payload
