#!/usr/bin/python3

# thunix_api.py
import flask

from flask import Flask, request, jsonify

import psutil, datetime, time, socket


app = Flask(__name__)


# No endpoint selected
@app.route("/")
def home():
    return "The Thunix API.  Please see https://wiki.thunix.net/wiki/api for more information."
    app.run()


# ip_info
@app.route("/ip_info")
def ip_info():
    def get_ip_addresses(family):
        for interface, snics in psutil.net_if_addrs().items():
            for snic in snics:
                if snic.family == family:
                    yield (interface, snic.address, snic.netmask)

    ipv4s = list(get_ip_addresses(socket.AF_INET))


    json_payload = "{\n\t\"Interfaces\":[\n"
    i = 0
    for i in range(len(ipv4s)) :
      json_payload = json_payload + "\t\t{\n"
      json_payload = json_payload + "\t\t\t\"Interface\":" + "\"" + ipv4s[i][0] + "\",\n"
      json_payload = json_payload + "\t\t\t\"Address\":" + "\"" + ipv4s[i][1] + "\",\n"
      json_payload = json_payload + "\t\t\t\"Netmask\":" + "\"" + ipv4s[i][2] + "\"\n"
      json_payload = json_payload + "\t\t}"
      i = i + 1
      if (i < len(ipv4s)) :
        json_payload = json_payload + ",\n"
      else:
        json_payload = json_payload + "\n"
    json_payload = json_payload + "\t]\n"
    json_payload = json_payload + "}\n"

    return json_payload
    app.run()


# uptime
@app.route("/uptime")
def uptime():
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
    loadavg = psutil.getloadavg()
    json_payload=[{"1min":loadavg[0], "5min":loadavg[1], "10min":loadavg[2]}]

    return jsonify(json_payload)
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
    return jsonify(teapots),418
    app.run()


# main loop
if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app

