#!/usr/bin/python3

"""Runner for thunix_api"""

from flask import Flask
from flask_restful import Api

from endpoints import disk, home, ip_info, load, memory, teapot, uptime

app = Flask(__name__) # pylint: disable=C0103
api = Api(app) # pylint: disable=C0103

api.add_resource(disk.Disk, "/disk")
api.add_resource(home.Home, "/")
api.add_resource(ip_info.IpInfo, "/ip_info")
api.add_resource(load.Load, "/load")
api.add_resource(memory.Memory, "/mem")
api.add_resource(teapot.Teapot, "/teapot")
api.add_resource(uptime.Uptime, "/uptime")

if __name__ == "__main__":
    app.run()
