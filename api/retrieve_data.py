import json
from operator import methodcaller
from index import app
from api.elastic_test import connect_elasticsearch
from flask import jsonify, request

es = connect_elasticsearch()

message = lambda m: { 'message':m }

@app.route('/', methods=['GET'])
def home():
    message = 'Flask is UP and RUNNING'
    return jsonify(message), 200

@app.route("/users",methods=["GET"])
def fetch_all_users():
  query_body = {
    "query": {
        "match_all": {}
    }
  }

  res = es.search(index="index_student", body=query_body)
  return jsonify(res),200


@app.route('/get_user', methods=['GET'])
def get_user():
    request_data = request.get_json()
    roll_no = request_data['roll_no']
    results = es.get(index='index_student', id=roll_no)
    return jsonify(results['_source']), 200


@app.route('/search_user', methods=['GET'])
def search_user():
    request_data = request.get_json()
    name = request_data['name']
    roll_no = request_data["roll_no"]
    

    query_body = {
        "query": {
            "dis_max": {
                "queries": [
                    {"match": {"name": name}},
                    {"match": {"roll_no": roll_no}}
                ],
                "tie_breaker": 0.3
            }
        }
    }

    res = es.search(index="index_student", body=query_body)
    print((res['hits']["total"]))
    if(res['hits']['total'] == 0):
      return jsonify(message("No data found")),400
    else:
      return jsonify(message(res['hits']['hits'][0]["_source"]))
