from pymongo import MongoClient

client = MongoClient('mongodb://wb-d-soasql2.web.local:27017')
db = client['taxonomy']
col = db['categories']


class MongoDBOperations:

    def __init__(self, tx_id):
        self.tx_id = tx_id

    def get_category_query(self):
        tx_qry = col.find({'CIAID': self.tx_id}, {'qry': 1, '_id': 0})
        for qry, ttl in tx_qry:
            print (qry['qry'], ttl['ttl'])
            return qry['qry'], ttl['ttl']

    def get_category_title(self):
        tx_ttl = col.find({'CIAID': self.tx_id}, {'ttl': 1, '_id': 0})
        for ttl in tx_ttl:
            return ttl['ttl']

