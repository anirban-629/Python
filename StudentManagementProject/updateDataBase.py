import pymongo
import docs

def main(data):
    client=pymongo.MongoClient(docs.URL)
    db=client[docs.DATABASE]
    collection=db[docs.COLLECTION]
    collection.insert_one()
    print('\nSuccessfull Updated ..!\n')