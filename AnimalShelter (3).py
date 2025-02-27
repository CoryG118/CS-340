#!/usr/bin/env python
# coding: utf-8

# In[54]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB datasets and collections.
        # This is hard-wired to use the aac database, the
        # animals collection and teh aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect 
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'aacuser'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34142
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data) #data should be dictionary
            #self.collection.insert_one(data)
            
        else: 
            raise Exception("Nothing to save, because data parameter is empty")
            
# Create method to implement the R in CRUD
    def read(self, query):
        if query is not None:
            results = list(self.database.animals.find(query)) #data should be dictionary
            return results
        else:
            raise Exception("Nothing to send, because query parameter is empty")
            
# Create method to implement the U in CRUD

    def update(self, query, new_vals):
        if query is not None:
                results = self.database.animals.update_many(query, {"$set": new_vals})
                return results.modified_count
        else:
            raise Exception("Nothing to update, because query parameter is empty")
        

#Create method to implement the D in CRUD

    def delete(self, query):
        if query is not None:
            results = self.database.animals.delete_many(query)
            return results.deleted_count


# In[55]:


crud = AnimalShelter()


# In[56]:


dog = {"animal_id": "T202201", "animal_type": "Dog", "breed": "Pitbull", "color": "White"}


# In[57]:


print(dog)


# In[58]:


crud.create(dog)


# In[59]:


crud.read(dog)


# In[60]:


query = {'animal_id': 'T202201'}
new_vals = {'color': 'White/Brown'}

modified_count = crud.update(query, new_vals)
print(modified_count)


# In[ ]:





# In[ ]:




