from fastapi import FastAPI
from app.controller.student import router
from app.model.student import init_db

init_db()

app = FastAPI(title="Students Service")
app.include_router(router)
