# -*- coding: utf-8 -*-

from flask import  Flask
from flask import jsonify
from flask import request
from flask_cors import CORS,cross_origin
from flask import  make_response
import places_api


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
       "origins": "*"
    }
})





@app.route('/', methods=['GET' , 'POST'])

def test():
    return "shay"

@app.route('/weekly_avg', methods=['GET' , 'POST'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
### Average Weekly PT for each Store
def weekly_avg():
    if request.method == 'OPTIONS': 
        return build_preflight_response()
    elif request.method == 'POST':
        data = request.get_json()

        x = places_api.weekly_avg_byID(data)
        x = jsonify(x)  
        # x.headers.add('Access-Control-Allow-Origin', '*')
        print(x)
        return x



@app.route('/daily_avg/<int:day>', methods=['GET' , 'POST','OPTIONS'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def daily_avg(day):
    if request.method == 'OPTIONS': 
        return build_preflight_response()
    elif request.method == 'POST':
        data = request.get_json()
        print(data)
        x = places_api.daily_avg_byID(data,day)
        x = jsonify(x)  

        print(x)
        return x

@app.route('/hourly_data/<int:day>/<int:hour>', methods=['GET' , 'POST','OPTIONS'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def hourly_data(day,hour):
    if request.method == 'OPTIONS': 
        return build_preflight_response()
    elif request.method == 'POST':
        data = request.get_json()
        print(data)
        x = places_api.hourly_data(data,day,hour)
        x = jsonify(x)  
        # x.headers.add('Access-Control-Allow-Origin', '*')
        return x


def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0')