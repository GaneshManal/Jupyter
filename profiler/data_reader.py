from elasticsearch import Elasticsearch


class ReadElasticData(object):
    def __init__(self, host='10.11.0.134'):
        self.host = host

    def read_data(self):
        data = {}

        es = Elasticsearch(host=self.host)
        cluster_info = es.search(index="testbulk", body={"size": 0, "query": {"bool": {"filter": [{"match": {"_plugin": "hostDatastore"}}]}}, "aggs": {"per_category": {"terms": {"field": "_clusterName"}}}})
        host_info = es.search(index="testbulk", body={"size": 0, "query": {"bool": {"filter": [{"match": {"_plugin": "Host"}}]}}, "aggs": {"per_category": {"terms": {"field": "_hostName"}, "aggs": {"Num VMs": {"top_hits": {"sort": [{"time": {"order": "desc"}}], "_source": {"includes": ["VMs"]},"size": 1}}}}}})

        cluster_df_data = cluster_info['aggregations']['per_category']['buckets']
        host_df_data = host_info['aggregations']['per_category']['buckets']

        cluster_list, host_list, vm_count_list = [], [], []
        for cluster in cluster_df_data:
            cluster_list.append(cluster['key'])

        for item in host_df_data:
            host_list.append(item['key'])
            vm_count_list.append(item['Num VMs']['hits']['hits'][0]['_source']['VMs'])

        data['Cluster'] = cluster_list
        data['Hosts'] = host_list
        data['VMs'] = vm_count_list
        return data
