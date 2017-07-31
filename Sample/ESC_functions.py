from datetime import datetime
from elasticsearch import Elasticsearch
import json


def read_data():
    es = Elasticsearch(host="10.11.0.199", port="9200")

    doc = {
        'author': 'Ganesh',
        'text': 'Elasticsearch: A sample Data read Example',
        'timestamp': datetime.now(),
    }

    # Read all the documents from the index - python_test_data
    '''
    res = es.search(index="python_test_data", doc_type="dknow", body={"query": {"match_all": {}}})
    print("%d documents found" % res['hits']['total'])
    '''

    # Read the specific documents from the index - python_test_data
    result = es.search(index="python_test_data", doc_type="dknow", size='10000', body={"query": {"match": {"hostName": "B"}}})
    # print('Result :', result, type(result))
    keys, data = [], []

    if len(result.get('hits').get('hits')) > 0:
        keys = result['hits']['hits'][0]['_source'].keys()
        for item in  result['hits']['hits']:
            data.append(item['_source'].values())
            # print item['_source']
            # data.append(item['_source'])

    # print("keys :", keys, type(keys))
    # print("Data :", data, type(data))
    return keys, data

'''
if __name__ == "__main__":
    x, y = read_data()
    print("Keys: ", json.dumps(x))
    print("Data: ", json.dumps(y))
'''