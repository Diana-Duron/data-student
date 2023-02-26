from Clases.DbMongo import DbMongo

class Careers:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self._id = id
        self._collection = "careers"
        
        
    db=DbMongo()
    
    ##CRUD##
    def create(self):
        careers_collection = self.db['careers']
        career_id = careers_collection.insert_one({
            'name': self.name
        }).inserted_id

        self._id = career_id  

    def update(self):
        careers_collection = self.db['careers']
        careers_collection.update_one({'_id': self._id}, {'$set': {'name': self.name}})

    def delete(self):
        careers_collection = self.db['careers']
        careers_collection.delete_one({'_id': self._id})