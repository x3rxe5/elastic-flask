from elasticsearch import Elasticsearch
from config.config_handling import get_config_value


def connect_elasticsearch(**kwargs):
  try:
      _es_config = get_config_value('elastic', 'es_host')
      _es_hosts = [_es_config]
      if 'hosts' in kwargs.keys():
          _es_hosts = kwargs['hosts']
      _es_obj = None
      _es_obj = Elasticsearch(hosts=_es_hosts, timeout=10)
      if _es_obj.ping():
          pass
      else:
          print('Awww it could not connect!')
      return _es_obj
  except Exception as e:
    print(e)

es = connect_elasticsearch()