# -*- coding: utf-8 -*-
from flask import Flask, request
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from flask import abort as flask_abort
import json

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/a')
def a():
    f = open('a.json')
    value = json.load(f)
    return jsonify(value)

@app.route('/b')
def b():
    f = open('b.json')
    value = json.load(f)
    return jsonify(value)

@app.route('/c')
def c():
    f = open('c.json')
    value = json.load(f)
    return jsonify(value)

@app.route('/d')
def d():
    f = open('d.json')
    value = json.load(f)
    return jsonify(value)



@app.route('/json1')
@auth.login_required
def get_json():
    dataSource = request.args.get('dataSource')
    if dataSource == 'Đẩy dữ liệu PYN':
        print(1111111111111111, dataSource)
    else:
        print(22222222222, dataSource)

    value = {
        "1": "một con vịt ịt ịt111111",
        "2": "hai con vịt11111111",
        "3": "ba con vịt",
        "4": "bốn con vịt",
        "5": "năm con vịt"
    }
    return jsonify(value)

@app.route('/json')
# @auth.login_required
def get_xml():
    flask_abort(500, 'xxxxxxxx')
    return "<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>"
	
@auth.verify_password
def authenticate(username, password):
	if username and password:
		if username == 'q' and password == 'q':
			return True
		else:
			return False
	return False
		
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
