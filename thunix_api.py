#!/usr/bin/python3

"""Runner for thunix_api"""
from flask import Flask
from flask_restful import Api

app = Flask(__name__) # pylint: disable=C0103
import disk, home, ip_info, load, memory, teapot, uptime
api = Api(app) # pylint: disable=C0103
api_version = "1"
url_prepend = "/api/v" + api_version
api.add_resource(disk.Disk, url_prepend +  "/disk")
api.add_resource(home.Home, url_prepend )
api.add_resource(ip_info.IpInfo, url_prepend + "/ip_info")
api.add_resource(load.Load, url_prepend + "/load")
api.add_resource(memory.Memory, url_prepend + "/mem")
api.add_resource(teapot.Teapot, url_prepend + "/teapot")
api.add_resource(uptime.Uptime, url_prepend + "/uptime")

if __name__ == "__main__":
    app.run()
