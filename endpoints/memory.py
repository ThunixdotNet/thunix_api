from flask_restful import Resource, abort
import psutil

class Memory(Resource):
    def get(self):
        vmem_usage = psutil.virtual_memory()
        smem_usage = psutil.swap_memory()
        json_payload={
          "total":vmem_usage.total,
          "free":vmem_usage.free,
          "used":vmem_usage.used,
          "percent":vmem_usage.percent
        }
        #abort(501, message="Not currently implemented.")
        return json_payload
