import json
from pprint import pprint
import os
import time

from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

class Search:
    def __init__(self, index_name = 'my_documents') -> None:
        self.es = Elasticsearch(os.environ['ELASTICSEARCH_URL'], 
                                basic_auth=(os.environ['BASIC_AUTH_USER'], os.environ['BASIC_AUTH_PASSWORD']),
                                ca_certs=os.environ['CA_CERT'])                                                                
        self.index_name = index_name
                                
        client_info = self.es.info()
        print('Connected to Elasticsearch')
        print(client_info.body)

    def create_index(self):
        self.es.indices.delete(index=self.index_name, ignore_unavailable=True)
        self.es.indices.create(index=self.index_name)

    def insert_document(self, document):
        return self.es.index(index=self.index_name, body=document)
    
    def insert_documents(self, documents):
        operations = []
        for document in documents:
            operations.append({'index': {'_index': f'{self.index_name}'}})
            operations.append(document)
        return self.es.bulk(operations=operations)
    
    def reindex(self):
        self.create_index()
        with open('data.json', 'rt') as f:
            documents = json.loads(f.read())
        return self.insert_documents(documents)
    
    def search(self, **query_args):
        return self.es.search(index=self.index_name, **query_args)
    
    def retrive_document(self, id):
        return self.es.get(index= self.index_name, id = id)