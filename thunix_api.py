#!/usr/bin/python3

from flask import Flask
from flask_restful import Resource, Api, abort

import datetime
import flask
import json
import psutil
import socket
import time

from endpoints import disk, home, ip_info, load, memory, teapot, uptime

app = Flask(__name__)
api = Api(app)

api.add_resource(disk.Disk, "/disk")
api.add_resource(home.Home, "/")
api.add_resource(ip_info.Ip_Info, "/ip_info")
api.add_resource(load.Load, "/load")
api.add_resource(memory.Memory, "/mem")
api.add_resource(teapot.Teapot, "/teapot")
api.add_resource(uptime.Uptime, "/uptime")

if __name__ == "__main__":
    app.run()
