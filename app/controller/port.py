from fastapi import APIRouter

port = APIRouter()

# http://localhost:8000/port
@port.get("/")
async def index10():
    return 2
