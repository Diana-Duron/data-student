from Clases.DbMongo import DbMongo
from Clases import Careers

class Courses:
    def __init__(self, id, name, career_id):
        self.name = name
        self.career_id = career_id
        self._id = id
        self._collection = "courses"
        
    db=DbMongo()
    
    ##CRUD##
    def create(self):
        courses_collection = self.db['courses']
        result = courses_collection.insert_one({
            'name': self.name,
            'career_id': self.career_id
        })

        self._id = result.inserted_id 

    def update(self):
        courses_collection = self.db['courses']
        courses_collection.update_one({'_id': self._id}, {'$set': {'name': self.name, 'career_id': self.career_id}})

    def delete(self):
        courses_collection = self.db['courses']
        courses_collection.delete_one({'_id': self._id})