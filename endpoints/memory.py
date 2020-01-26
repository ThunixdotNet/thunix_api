from flask_restful import Resource, abort
import psutil

class Memory(Resource):
    def get(self):
        vmem_usage = psutil.virtual_memory()
        smem_usage = psutil.swap_memory()
        abort(501, message="Not currently implemented.")
