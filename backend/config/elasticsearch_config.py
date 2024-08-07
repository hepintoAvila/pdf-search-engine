from elasticsearch import Elasticsearch

es = Elasticsearch()

def index_document(doc_id, text):
    es.index(index='documents', id=doc_id, body={'text': text})
