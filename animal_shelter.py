from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    #CRUD operation for Animal collection in MongoDB
    def __init__(self, username, password):
        #Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:53383/AAC' % (username, password))
        self.database = self.client['AAC']
        
        #complete this method for the C in crud.
        def create(self, data):
            #Checks to see if the data is null or empty and returns false in either case
            if data is not None:
                if data:
                    self.database.animals.insert_one(data)
                    return True
            else:
                return False
            
        def read(self, search): 
            #Checks to see if the data is null or empty and returns exception in either case
            if search is not None:
                if search:
                    searchResult = self.database.animals.find(search)
                    return searchResult
                else:
                    exception = "Nothing to search, because search parameter is empty."
                    return exception
        
        #The update(self,data) method   
        def update(self, data):
            if data is not None:
                self.database.animals.save(data.get_as_json())
            else:
                updateException = "No results found."
                return updateException
        
        #The delete(self,data) method
        def delete(self, data):
            if data is not None:
                self.database.animals.remove(data.get_as_json())
            else:
                deleteException = "Nothing to delete."
                return deleteException  