import json
import sys
from flask import Flask
#from sense_hat import SenseHat

#init Sense Hat 
# sense = SenseHat()
# sense.clear()

app = Flask(__name__)

def getSensePiCelciusTemp():
    # sense.clear()
    # temperature = sense.get_temperature()
    temperature = 23.88889
    return temperature

def getSensePiHumidity():
    # sense.clear()
    # humidity = sense.get_humidity()
    humidity = 72.88889
    return humidity

def getSensePiPressure():    
    # sense.clear()
    # barPressure = sense.get_pressure()
    barPressure = 1037.033333
    # Convert sense hat millibar pressure into inMg (best for determining if it matters or not)  
    inchesMercuryPressure = barPressure * 0.0295300
    return inchesMercuryPressure

@app.route('/')
def index():
    return json.dumps({'name': 'Json', 'framework': 'Flask'})

@app.route('/getCelcius',methods=['GET'])
def getCelciusTemperature():
    temperature = getSensePiCelciusTemp()
    return json.dumps({'temperature': temperature})

@app.route('/getHumidity',methods=['GET'])
def getHumidity():
    humidity = getSensePiHumidity()
    return json.dumps({'temperature': humidity})

@app.route('/getPressure',methods=['GET'])
def getBarometricPressure():
    inchesMercuryPressure = getSensePiPressure()
    return json.dumps({'pressure': inchesMercuryPressure})

@app.route('/getAll', methods=['GET'])
def getAll():
    temp = getSensePiCelciusTemp()
    humidity = getSensePiHumidity()
    pressure = getSensePiPressure()
    return json.dumps({'temperature':temp, 'humidity': humidity, 'pressure': pressure})

host='0.0.0.0'
port=7866
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--develop':
        app.run(host,port, debug=True)
    else:
        app.run(host, port, debug=False)

app.run(host = '0.0.0.0', port=7866, debug=True)