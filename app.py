from flask import Flask, json,request,jsonify

app = Flask(__name__)


# devices=[
#     {'id': 0,
#      'name': 'GM IoT',
#      'temperature': '30°C',
#      'humidity': '84%',
#      },
# ]

@app.route("/")
def home():
    return "Welcome to Grain Manager API"


@app.route("/devices",methods=["GET"])
def getDevices():
    f=open("data.json","r")
    devices = json.loads(f.read())
    f.close()
    print(jsonify(devices))
    return jsonify(devices)

@app.route("/editdata/<id>",methods=["POST"])
def editDeviceData(id):
    input_json = request.get_json(force=True)
    f=open("data.json","r")
    devices = json.loads(f.read())
    f.close()
    for device in devices:
        if int(id) == device["id"]:
            device["name"]=input_json['name']
            device["temperature"]=input_json['temperature']
            device["humidity"]=input_json['humidity']
    f=open("data.json","w")
    jsonString= json.dumps(devices)
    f.write(jsonString)
    f.close()
    dictToReturn = {'editSuccessful':True}
    return jsonify(dictToReturn)

@app.route('/test',methods=['POST'])
def testing():
    input_json = request.get_json(force=True)
    print(json.dumps(input_json))

    return jsonify(input_json)

if __name__ == '__main__':
    app.run(threaded=True,port=8000)
