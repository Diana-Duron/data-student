from Clases import Students, Courses, DbMongo

class Enrollments:
    def __init__(self, student_id, course_id, passed, id):
        self.student_id = student_id
        self.course_id = course_id
        self.passed = passed
        self._id = id
        self._collection = 'enrollments'
        
    db=DbMongo()

    ##CRUD##
    def create(self):
        enrollments_collection = self.db['enrollments']

        result = enrollments_collection.insert_one({
            'student_id': self.student_id,
            'course_id': self.course_id,
            'passed': self.passed
        })

        self._id = str(result.inserted_id)  


    def update(self):
        enrollments_collection = self.db['enrollments']
        enrollments_collection.update_one({'_id': self._id}, {'$set': {'student_id': self.student_id, 'course_id': self.course_id, 'passed': self.passed}})

    def delete(self):
        enrollments_collection = self.db['enrollments']
        enrollments_collection.delete_one({'_id': self._id})
        