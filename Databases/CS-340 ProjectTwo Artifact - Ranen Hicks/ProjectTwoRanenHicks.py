from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, USER, PASS): #, HOST, PORT, DB, COL):
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
        #USER = 'aacuser'
        #PASS = 'aacPass'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31870
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# This method allows the user to insert an animal into the database
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary    
            return "True"  # Feedback to user.
        else:
            return "False"

# This method allows the user to search an AAC database for specific animals.
    def read(self, data):
        if data is not None:
            result = self.database.animals.find(data)  # Result stored in list.
            result2 = list(result)
            print("[")
            return result2
            print("]")
        
        else:
            print("[]") #Creating an empty list using brackets.
    
#  This method allows the user to update all queries that match their first input with what they want to change as their second.
    def update(self, data, data2):
        if data is not None:
                #  Only need to use update_many as it can do one and many updates. It also reduces the amount of code written.
                result = self.database.animals.update_many(data, data2)
                return result.modified_count
        else:
            return 0
    
#  This method allows the user to delete all the queries that match the input they entered into the funciton.
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)
            return result.deleted_count
        else:
            return 0