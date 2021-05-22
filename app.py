from re import DEBUG
from flask import Flask, json,request,jsonify

app = Flask(__name__)


devices=[
    {'id': 0,
     'name': 'GM IoT',
     'temperature': '30°C',
     'humidity': '84%',
     },
]

@app.route("/")
def home():
    return "Welcome to Grain Manager API"

@app.route("/devices",methods=["GET"])
def getDevices():
    return jsonify(devices)

@app.route("/editdata/<id>",methods=["POST"])
def editDeviceData(id):
    input_json = request.get_json(force=True)

    for device in devices:
        if int(id) == device["id"]:
            device["name"]=input_json['name']
            device["temperature"]=input_json['temperature']
            device["humidity"]=input_json['humidity']
            return jsonify(device)

    dictToReturn = {'editSuccessful':True}
    return jsonify(dictToReturn)

if __name__ == '__main__':
    app.run(threaded=True,port=8000)
