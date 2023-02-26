from Clases.DbMongo import DbMongo
from Clases import Careers
from Clases import DATA, Dataprocess

class Students:
    def __init__(self, id, name, age, career_id):
        self.name = name
        self.age = age
        self.career_id = career_id
        self._id = id
        self._collection = "students"

    db=DbMongo()

    ##CRUD##
    def create(self):
        students_collection = self.db['students']

        # Insertar el nuevo estudiante en la colección de estudiantes
        result = students_collection.insert_one({
            'name': self.name,
            'age': self.age,
            'career_id': self.career_id
        })

        self._id = str(result.inserted_id)  

    def update(self):
        
        students_collection = self.db['students']

        # Actualizar el estudiante en la colección de estudiantes
        students_collection.update_one({'_id': self._id}, {'$set': {'name': self.name, 'age': self.age, 'career_id': self.career_id}})

    def delete(self):
        students_collection = self.db['students']

        # Eliminar el estudiante de la colección de estudiantes
        students_collection.delete_one({'_id': self._id})
        