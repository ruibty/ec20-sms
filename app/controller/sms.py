from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.db.models import get_items
from app.modem import send_sms

sms = APIRouter(
    prefix='/sms'
)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# http://localhost:8085/sms/
@sms.post("/")
def create_user(body: dict, db: Session = Depends(get_db)):
    print(body)
    tel_num, content = body['tel_num'], body['content']
    db_sms = send_sms(tel_num, content)
    return db_sms


# http://localhost:8085/sms/by-type/1?page=1&row=50
@sms.get("/by-type/{type}")
async def get_type(type: int = 1, page: int = 1, row: int = 50, db: Session = Depends(get_db)):
    skip = (page - 1) * row
    return get_items(db, type=type, skip=skip, limit=row)
