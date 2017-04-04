import pysolr


class SolrOperations:

    con = pysolr.Solr('http://localhost:8983/solr/discovery')

    def __init__(self, connection, iaid):
        self.tx_ttl = ''
        self.tx_id = ''
        self.iaid = iaid
        self.q = ''
        self.src_tna = 'SOURCE:100 OR SOURCE:200 AND '
        self.src_a2a = 'SOURCE:600 AND '
        self.con = connection

    def add_taxonomy(self):
        docs = {'DOCREFERENCE': self.iaid, 'TAXONOMY': self.tx_id + ' ' + self.tx_ttl, 'TAXONOMYID': self.tx_id}
        for doc in docs:
            self.con.add([doc], fieldUpdates={'TAXONOMY': 'add', 'TAXONOMYID': 'add'})

    def remove_taxonomy(self):
        docs = {'DOCREFERENCE': self.iaid, 'TAXONOMY': self.tx_id + ' ' + self.tx_ttl, 'TAXONOMYID': self.tx_id}
        for doc in docs:
            self.con.add([doc], fieldUpdates={'TAXONOMY': 'remove', 'TAXONOMYID': 'remove'})

# Search query to find results where document is not tagged + matches query (tna)
    def find_not_tagged_tna(self):
        results = self.con.search(self.src_tna + 'DOCREFERENCE:' + self.iaid + ' AND ' + self.q + ' NOT TAXONOMYID:'
                                  + self.tx_id)
        print("Docs Found, not tagged {0} Result(s).".format(len(results)))
        for result in results:
            print("IAID: '{0}'.".format(result['DOCREFERENCE']))
            return self.iaid
    find_not_tagged_tna()

# search query to find results where document is tagged + no longer matches query (tna)
    def find_is_tagged_tna(self):
        results = self.con.search(self.src_tna + 'DOCREFERENCE:' + self.iaid + ' AND TAXONOMYID:' + self.tx_id + ' NOT '
                                  + self.q)
        print("Docs Found, tagged {0} Result(s).".format(len(results)))
        for result in results:
            print("IAID: '{0}'.".format(result['DOCREFERENCE']))
            return self.iaid
    find_is_tagged_tna()

# Search query to find results where document is not tagged + matches query (a2a)
    def find_not_tagged_a2a(self):
        results = self.con.search(self.src_a2a + 'DOCREFERENCE:' + self.iaid + ' AND ' + self.q + ' NOT TAXONOMYID:'
                                  + self.tx_id)
        print("Docs Found, not tagged {0} Result(s).".format(len(results)))
        for result in results:
            print("IAID: '{0}'.".format(result['DOCREFERENCE']))
            return self.iaid
    find_not_tagged_a2a()

# search query to find results where document is tagged + no longer matches query (a2a)
    def find_is_tagged_a2a(self):
        results = self.con.search(self.src_a2a + 'DOCREFERENCE:' + self.iaid + ' AND TAXONOMYID:' + self.tx_id + ' NOT '
                                  + self.q)
        print("Docs Found, tagged {0} Result(s).".format(len(results)))
        for result in results:
            print("IAID: '{0}'.".format(result['DOCREFERENCE']))
            return self.iaid
    find_is_tagged_a2a()