from index import app
from api.elastic_test import connect_elasticsearch
from flask import request
from flask import jsonify

es = connect_elasticsearch()

@app.route('/add_user', methods=['POST'])
def add_user():
    request_data = request.get_json()
    name = request_data['name']
    gender = request_data['gender']
    roll_no = request_data['roll_no']
    nationality = request_data['nationality']

    user_obj = {
        "name":name,
        "gender":gender,
        "roll_no":roll_no,
        "nationality":nationality
    }

    result = es.index(index='index_student', id=roll_no, body=user_obj, request_timeout=30)
    return jsonify(result),200

@app.route('/update_user', methods=['POST'])
def update_user():
    user_id = request.form['id']
    param = request.form['param']
    new_val = request.form['new_value']

    update_dict = {
        'doc':{
            param: new_val
        }
    }

    response = es.update(index='user', id=user_id, body=update_dict)
    return jsonify(response)