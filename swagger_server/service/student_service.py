from tinydb import Query, TinyDB

db = TinyDB('db.json')

def add(body):
    db.insert(body.to_dict())
    return 200, 'ok'

def delete(student_id):
    db.remove(Query().id == student_id)
    return 200, 'ok'

def get(student_id):
    return db.get(Query().id == student_id)

