from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class StudentBody(BaseModel):
    first_name: str
    last_name: str
    age: int
    courses: list[str]

app = FastAPI(title="Students Accounting API")

courses = {
        1: {"id": 1, "name": "Python"},
        2: {"id": 2, "name": "Backend"},
        3: {"id": 3, "name": "AI"}
}
students = {}

@app.post("/students")
def create_student(student: StudentBody):
     new_id = max (students.keys(), default = 0) + 1
     new_student = {"id": new_id, **student.model_dump()}
     students[new_id] = new_student
     return new_student

@app.delete("/students/{student_i}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    deleted_student = students.pop(student_id)
    return deleted_student

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code = 404, detail="student not found")
    return students[student_id]

@app.get("/students")
def get_all_students():
    return list(students.values())

@app.patch("/students/{student_id}")
def update_student(student_id: int, student: StudentBody):
    updated_student = {"id": student_id, **student.model_dump()}
    students[student_id] = updated_student
    return updated_student
