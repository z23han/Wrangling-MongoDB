from autos import process_file
from pprint import pprint

def insert_autos(infile, db):
    autos = process_file(infile)
    # Your code here. Insert the data in one command
    db.autos.insert(autos)
    # autos will be a list of dictionaries, as in the example in the previous video
    # You have to insert data in a collection 'autos'

  
if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    insert_autos('autos-small.csv', db)
    pprint(db.autos.find_one())