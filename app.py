import pymongo
from Clases import DATA, Dataprocess
#from Clases.Careers import Careers
from Clases.Courses import Courses
from Clases.Students import Students
from Clases.Enrollments import Enrollments
from Clases.DbMongo import DbMongo
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    #Conexión a la base de datos
    bd=DbMongo()
    
    #Lectura de datos
    pipeline = Dataprocess(DATA)
    
    #Migración de datos
    pipeline.create_careers(bd)
    pipeline.create_students(bd)
    pipeline.create_enrollments(bd)
    
    # Reporte de cantidad de estudiantes por carrera
    print("Cantidad de estudiantes por carrera:")
    print(Enrollments.count_students_by_career(bd))
    
    # Reporte histórico de aprobados y reprobados por curso
    print("\nHistórico de aprobados y reprobados por curso:")
    print(Students.report_approved_rejected_by_course(bd))

    return
if __name__ == "__main__":
    main()