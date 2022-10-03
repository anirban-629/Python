import pymongo
import docs

def main():
    client=pymongo.MongoClient(docs.URL)
    db=client[docs.DATABASE]
    collection=db[docs.COLLECTION]
    name=input('Enter your name in short (like-> F.LastName) -> ')
    collection.insert_one(
        {   '_id':f'GMIT-DATABASE({name})',
            'Project-Name':'Student Management',
            'Project-Code':'abc123'
        },
    )
    print('Initialization Successfull')
