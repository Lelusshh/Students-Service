courses = {
        1: {"id": 1, "name": "Python"},
        2: {"id": 2, "name": "Backend"},
        3: {"id": 3, "name": "AI"}
}
students = {}
def create_student(student: StudentBody):
     new_id = max (students.keys(), default = 0) + 1
     new_student = {"id": new_id, **student.model_dump()}
     students[new_id] = new_student
     return new_student

def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    deleted_student = students.pop(student_id)
    return deleted_student

def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code = 404, detail="student not found")
    return students[student_id]

def get_all_students():
    return list(students.values())

def update_student(student_id: int, student: StudentBody):
    updated_student = {"id": student_id, **student.model_dump()}
    students[student_id] = updated_student
    return updated_student
