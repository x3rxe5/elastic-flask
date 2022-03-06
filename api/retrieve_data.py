from index import app
from api.elastic_test import connect_elasticsearch
from flask import jsonify, request

es = connect_elasticsearch()

@app.route('/', methods=['GET'])
def home():
    message = 'Flask is UP and RUNNING'
    return jsonify(message),200


@app.route('/get_user', methods=['GET'])
def get_user():
    request_data = request.get_json()    
    roll_no = request_data['roll_no']    
    results = es.get(index='index_student', id=roll_no)
    return jsonify(results['_source']),200

# @app.route("/user",method=["GET"])
# def fetch_all_user():
#   results = es.index(index='index_student')
#   return jsonify(results['_source']),200

@app.route('/search_user', methods=['GET'])
def search_user():
    request_data = request.get_json()    
    keyword = request_data['keyword']
    # keyword = request.form['keyword']

    query_body = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["name", "roll_no"]
            }
        }
    }

    res = es.search(index="user", body=query_body)

    return jsonify(res['hits']['hits'])