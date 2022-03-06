# Flask and ElasticSearch Demo

### 1) Setup a virtual environment for targeted folder
```bash
$ pip install virtualenv

$ virtualenv env

# and now activate it
$ source ./bin/activate
```

### 2) First create config.ini file in ./config folder and paste this code
  ```bash
      [elastic]
      es_host = <your host and port>
      e.g. eg_host = http://localhost:9200

      [kibana]
      kibana_host = <your host and port>
  ```

### 3) add the dependency requirements using requirements.txt file 
```bash 
$ pip install -r requirements.txt
```
