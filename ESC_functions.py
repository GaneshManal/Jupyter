from datetime import datetime
from elasticsearch import Elasticsearch

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
    res = es.search(index="python_test_data", doc_type="dknow", size='10000', body={"query": {"match": {"hostName": "B"}}})

    data = []
    for item in  res['hits']['hits']:
        data.append(item['_source'].values())
        # print item['_source']
        # data.append(item['_source'])

    return data
