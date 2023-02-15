import os
import tempfile
from functools import reduce

import pymongo

# from tinydb import Query, TinyDB


# db_dir_path = tempfile.gettempdir()
# db_file_path = os.path.join(db_dir_path, "students.json")
# student_db = TinyDB(db_file_path)

# Create a local MongoDB database
print(os.getenv('MONGO_URI'))
myclient = pymongo.MongoClient(os.environ['MONGO_URI'])
mydb = myclient["mydatabase"]
mycol = mydb["students"]



# def add(student=None):
#     queries = []
#     query = Query()
#     queries.append(query.first_name == student.first_name)
#     queries.append(query.last_name == student.last_name)
#     query = reduce(lambda a, b: a & b, queries)
#     res = student_db.search(query)
#     if res:
#         return 'already exists', 409

#     doc_id = student_db.insert(student.to_dict())
#     student.student_id = doc_id
#     return student.student_id


def add(student=None):
    # Check if student already exists
    myquery = {"first_name": student.first_name, "last_name": student.last_name}
    mydoc = mycol.find(myquery)
    if mydoc:
        return 'already exists', 409

    mydict = student.to_dict()
    x = mycol.insert_one(mydict)
    return student.student_id


# def get_by_id(student_id=None, subject=None):
#     student = student_db.get(doc_id=int(student_id))
#     if not student:
#         return 'not found', 404
#     student['student_id'] = student_id
#     print(student)
#     return student


def get_by_id(student_id=None, subject=None):
    myquery = {"_id": student_id}
    mydoc = mycol.find(myquery)

    if not mydoc:
        return 'not found', 404
    
    print(mydoc[0])
    return mydoc[0]


# def delete(student_id=None):
#     student = student_db.get(doc_id=int(student_id))
#     if not student:
#         return 'not found', 404
#     student_db.remove(doc_ids=[int(student_id)])
#     return student_id

def delete(student_id=None):
    myquery = {"_id": student_id}
    mydoc = mycol.find(myquery)

    if not mydoc:
        return 'not found', 404
    
    mycol.delete_one(myquery)
    return student_id