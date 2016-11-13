import matplotlib.pyplot as plot
from house import *

if __name__ == '__main__':
    devicelist = [device(0.01, 20, 2, 100), device(0.03, 900, 100, 20), device(0.005, 59, 2, 60)]
    house1 = house(devicelist)
    data = []
    for i in range(9000):
        house1.update(1)
        data.append(house1.watts())

    plot.plot(range(9000), data)
    plot.show()


#from flask import Flask
#import os

#app = Flask(__name__)

#port = int(os.getenv("PORT", 64781))

#@app.route('/')
#def hello_world():
#    return 'Python Predix.io - Hello World Example'

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=port)
