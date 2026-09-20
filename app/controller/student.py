from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import app.model.student as model
from app.view.student import StudentBody

router = APIRouter(prefix="/students", tags=['students'])

@router.post("")
def create_student(student: StudentBody):
    return model.create_student(student)

@router.delete("/{student_id}")
def delete_student(student_id):
    return model.delete_student(student_id)

@router.get("/{student_id}")
def get_student(student_id: int):
    return model.get_student(student_id)

@router.get("")
def get_all_students():
    return model.get_all_students()

@router.patch("/{student_id}")
def update_student(student_id: int, student: StudentBody):
    return model.update_student(student_id, student)

