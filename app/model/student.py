from pathlib import Path
from sqlalchemy import (JSON, Column, Integer, MetaData, String, Table, create_engine, inspect, select)
from app.view.student import StudentBody
from fastapi import HTTPException

db_path = Path (__file__).resolve().parents[2] / "students.db"
engine = create_engine(f"sqlite:///{db_path}")


metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key = True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("age", Integer, nullable=False),
    Column("courses", JSON, nullable=False),
)


def init_db():
    with engine.begin() as connection:
        if inspect(connection).has_table("students"):
            return
        metadata.create_all(connection)



def create_student(student: StudentBody):
    query = students.insert().values(**student.model_dump())
    with engine.begin() as connect:
        result = connect.execute(query)
        return {"id": result.inserted_primary_key[0], **student.model_dump()}


def delete_student(student_id: int):
    check_query = students.select().where(students.c.id == student_id)
    query = students.delete().where(students.c.id == student_id)

    with engine.begin() as connect:
        existing_student = connect.execute(check_query).first()
        if not existing_student:
            raise HTTPException(status_code=404, detail="Student not found")
        
        connect.execute(query)
        return {"message": f"User {student_id} deleted successfully!"}


def get_student(student_id: int):
    query = students.select().where(students.c.id == student_id)

    with engine.connect() as connect:
        result = connect.execute(stmt).mappings().first()
    
    if not result:
        raise HTTPException(status_code = 404, detail="student not found")
    return dict(result)
    

def get_all_students():
    query = students.select()

    with engine.connect() as connect:
        results = connect.execute(query).mappings().all()
        return [dict(row) for row in results]


def update_student(student_id: int, student: StudentBody):
    check_query = students.select().where(students.c.id == student_id)
    query = students.update().where(students.c.id == student_id).values(**student.model_dump())

    with engine.begin() as connect:
        existing_student = connect.execute(check_query).first()
        if not existing_student:
            raise HTTPException(status_code=404, detail="User not found")

        connect.execute(query)
        return {"id": student_id, **student.model_dump()}
