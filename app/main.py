from fastapo import FastAPI
from app.model.student import init_db
init_db()
app = FastAPI(title="Students Service")
