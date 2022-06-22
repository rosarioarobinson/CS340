from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:52396' % (username, password))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            # code taken from Mastering MongoDB, page 92
            insert_result = self.database.animals.insert_one(data)  # data should be dictionary
            #pprint(insert_result)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self, data):
        if data is not None:
            # code taken from Mastering MongoDB, page 92
            result = self.database.animals.find(data, {"_id": False})
            #pprint(result)
            return result
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
# Update method to implement the U in CRUD.
    def update(self, data, newValues):
        if data is not None:
            result = self.database.animals.update_one(data, {'$set': newValues})
            return True
        else:
            raise Exception("Nothing to update, because data parameter is empty")

# Delete method to implement the D in CRUD.
    def delete(self, data):
        if data is not None: 
            result = self.database.animals.delete_one(data)
            return True
        else:
            raise Exception("Nothing to delete, because data parameter is empty")