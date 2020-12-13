# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import places_api

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET' , 'POST'])

def test():
    return "shay"


@app.route('/test', methods=['GET' , 'POST'])

def search():
    data = request.get_json()
    print(data)
    x = places_api.weekly_avg_for_each_ID(data)
    x = jsonify(x)  
    return x 



@app.route('/daily_avg_byID/<string:ID>/<int:day>/', methods=['GET' , 'POST'])

def daily_avg_byID(ID,day):#send Place_ID and index of day Monday is represented by 0
    x = places_api.daily_avg_byID(ID,day)
    x = jsonify(x)
    return x

@app.route('/weekly_avg_byID/<string:ID>/', methods=['GET' , 'POST'])
def weekly_avg_byID(ID):
    x = places_api.weekly_avg_byID(ID)
    x = jsonify(x)  
    return x



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)