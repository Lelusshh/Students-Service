from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.model import category as model
from app.view.category import StudentBody

@app.post("/students")
def create_student(student: StudentBody):
    return model.create_student(student)

@app.delete("/students/{student_i}")
def delete_student(student_id):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return model.delete_student(student_id: int)

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code = 404, detail="student not found")
    return model.get_student(student_id)

@app.get("/students")
def get_all_students():
    return model.list(students.values())

@app.patch("/students/{student_id}")
def update_student(student_id: int, student: StudentBody):
    return model.update_student(student_id, student)

