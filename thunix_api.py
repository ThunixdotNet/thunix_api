# thunix_api.py
import flask

from flask import Flask, request, jsonify

import psutil, datetime


app = Flask(__name__)


# No endpoint selected
@app.route("/")
def home():
    return "The Thunix API.  Please see https://wiki.thunix.net/wiki/api for more information."
    app.run()


# ip_info
@app.route("/ip_info")
def ip_info():
    return "IP Info"
    app.run()


# uptime
@app.route("/uptime")
def uptime():

    return str(datetime.timedelta(seconds=psutil.boot_time()))
    app.run()


# teapot
@app.route("/teapot")
def teapot():
    teapots = [
        {
            "tea": "available",
            "height": "short",
            "width": "stout"
        }
    ]
    return jsonify(teapots)
    app.run()


# main loop
if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app

