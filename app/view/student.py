from pydantic import BaseModel

class StudentBody(BaseModel):
    first_name: str
    last_name: str
    age: int
    courses: list[str]
