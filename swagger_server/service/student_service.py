import os
import tempfile
from functools import reduce

# import pymongo
from bson.objectid import ObjectId

# Create a local MongoDB database
print(os.getenv('MONGO_URI'))
myclient = pymongo.MongoClient(os.environ.get('MONGO_URI', default='mongodb://localhost:27017'))
mydb = myclient["mydatabase"]
mycol = mydb["students"]


def add(student=None):
    # Check if student already exists
    myquery = {"first_name": student.first_name, "last_name": student.last_name}
    mydoc = mycol.find(myquery)

    if len(list(mydoc)) > 0:
        return 'already exists', 409

    mydict = student.to_dict()
    x = mycol.insert_one(mydict)
    return str(x.inserted_id)


def get_by_id(student_id=None, subject=None):
    myquery = {"_id": ObjectId(str(student_id))}
    mydoc = mycol.find_one(myquery)

    if not mydoc:
        return 'not found', 404
    
    # Remove the _id field from the dictionary
    del mydoc['_id']

    return mydoc


def delete(student_id=None):
    myquery = {"_id": ObjectId(str(student_id))}
    mydoc = mycol.find_one(myquery)

    if not mydoc:
        return 'not found', 404
    
    mycol.delete_one(myquery)
    return str(student_id)