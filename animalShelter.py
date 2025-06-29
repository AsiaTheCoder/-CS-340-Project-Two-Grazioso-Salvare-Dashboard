from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # Connection
        USER = 'aacuser'
        PASS = 'Snhu1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31325
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d/admin' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Creates method to implement the C in CRUD
    def create(self, data):
        try:
            if data is not None:
                insert_result = self.collection.insert_one(data) # Inserts the document
                return insert_result.acknowledged # True if the insert succeeds
            else:
                raise ValueError("Nothing to save, because data parameter is empty")
        except Exception as e:
            print(f"An error has occurred while inserting: {e}")
            return False

# Creates method to implement the R in CRUD
    def read(self, query):
        # query is a dictionary used in the find() method
        try:
            if query is not None:
                results = self.collection.find(query)
                return list(results) # Returns results as a list
            else:
                raise ValueError("Nothing to search, because query parameter is empty")
        except Exception as e:
            print(f"An error occurred while reading: {e}")
            return []
        
#Creates method to implement the U in CRUD
    def update(self, query, new_values):
        # query is a dictionary used in the update_many() method
        try:
            if query is not None and new_values is not None: 
                update_result = self.collection.update_many(query, {'$set': new_values})
                return update_result.modified_count
            else:
                raise ValueError("Query and/or new values are empty")
        except Exception as e:
            print(f"An error occurred while updating: {e}")
            return 0
        
#Creates method to implement the D in CRUD
    def delete(self, query):
        # query is a dictionary used in the delete_many() method
        try:
            if query is not None:
                delete_result = self.collection.delete_many(query)
                return delete_result.deleted_count
            else:
                raise ValueError("Nothing to delete, because query parameter is empty")
        except Exception as e:
            print(f"An error occurred while deleting: {e}")
            return 0
