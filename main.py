import matplotlib.pyplot as plot
from house import *

from flask import Flask
from flask_cors import CORS, cross_origin
import os
import csv

import threading
import time

app = Flask(__name__)
CORS(app)

port = int(os.getenv("PORT"))

data = dict()

def dataUpdate():
    if __name__ == '__main__':
        devicelist = [device(0.01, 20, 2, 100), device(0.03, 900, 100, 20), device(0.005, 59, 2, 60)]
        house1 = house(devicelist)

        while True:
            house1.update(1)
            data[int(time.time())] = house1.watts()
            time.sleep(1)

@app.route('/')
def hello_world():
    result = "{ \"BIGDD\": ["
    for key in data:
        result += "{"
        result += "\"timestamp\": " + str(key) + ","
        result += "\"value\": " + str(data[key]) + "},"
    result = result.rstrip(',')
    result += "]}"
    return result.replace("'", '"')

if __name__ == '__main__':
    threading.Thread(target=dataUpdate).start()
    app.run(host='0.0.0.0', port=port)
