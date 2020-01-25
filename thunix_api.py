#!/usr/bin/python3

# thunix_api.py
import flask

from flask import Flask, request, jsonify

import psutil, datetime, time, socket, json


app = Flask(__name__)


# No endpoint selected
@app.route("/")
def home():
    print ("Content-Type: application/json\n")
    payload = [{"Description":"The Thunix API.  Please see https://wiki.thunix.net/wiki/api for more information."}]
    return jsonify(payload) 
    app.run()


# ip_info
@app.route("/ip_info")
def ip_info():
    print ("Content-Type: application/json\n")
    def get_ip_addresses(family):
        for interface, snics in psutil.net_if_addrs().items():
            for snic in snics:
                if snic.family == family:
                    yield (interface, snic.address, snic.netmask)

    ipv4s = list(get_ip_addresses(socket.AF_INET))


    payload = "{\"Interfaces\":["
    i = 0
    for i in range(len(ipv4s)) :
      payload = payload + "{"
      payload = payload + '"Interface":' + '"' + ipv4s[i][0] + '",'
      payload = payload + '"Address":' + '"' + ipv4s[i][1] + '",'
      payload = payload + '"Netmask":' + '"' + ipv4s[i][2] + '"'
      payload = payload + "}"
      i = i + 1
      if (i < len(ipv4s)) :
        payload = payload + ","
      else:
        payload = payload + ""
    payload = payload + "]"
    payload = payload + "}"
    payload = json.loads(payload)
    return jsonify(payload)
    app.run()


# uptime
@app.route("/uptime")
def uptime():
    print ("Content-Type: application/json\n")
    with open('/proc/uptime', 'r') as f:
      secs = float(f.readline().split()[0])
    day = secs // (24 * 3600)
    secs = secs % (24 * 3600)
    hour = secs // 3600
    secs %= 3600
    minutes = secs // 60
    secs %= 60
    seconds = secs 
    payload = [
        {
          "days": day,
          "hours": hour,
          "minutes": minutes,
          "seconds": seconds
        }
    ]
    return jsonify(payload)
        
    app.run()

# load avg
@app.route("/load")
def loadaverage():
    print ("Content-Type: application/json\n")
    loadavg = psutil.getloadavg()
    payload=[{"1min":loadavg[0], "5min":loadavg[1], "10min":loadavg[2]}]

    return jsonify(payload)
    app.run()

# teapot
@app.route("/teapot")
def teapot():
    print ("Content-Type: application/json\n")
    teapots = [
        {
            "tea": "available",
            "height": "short",
            "width": "stout"
        }
    ]
    return jsonify(teapots),418
    app.run()


# main loop
if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app

