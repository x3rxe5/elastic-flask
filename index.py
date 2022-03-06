from flask import Flask

# databse connection
from api.elastic_test import connect_elasticsearch

es = connect_elasticsearch()

app = Flask(__name__)

@app.route("/first",methods=["GET"])
def index_first():
  return "Hello World"


from api.insert_data import *
from api.retrieve_data import *



if __name__ == "__main__":
  app.run(debug=True)

