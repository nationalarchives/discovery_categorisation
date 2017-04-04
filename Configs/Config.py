class Config:
    """Class to contain project level constants and attributes
    Should be imported in to every module"""
    MONGODB_SERVER = "wb-solrnutch1.web.local"
    MONGODB_PORT = "27017"
    MONGODB_DATABASE = "taxonomy"
    MONGODB_COLLECTION = "categories"

    SOLR_SERVER = "wb-solrnutch1.web.local"
    SOLR_PORT = "8986"
    SOLR_CORE = "DISCOVERY"
