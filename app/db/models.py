from sqlalchemy import Column, String, BigInteger, SmallInteger
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import Session

from .database import Base


class Sms(Base):
    __tablename__ = 'm_sms'  # 数据库表名

    sms_id = Column(BigInteger, primary_key=True, index=True)
    # account = Column(String(255), unique=True, index=True),index=True)
    # 1 代表发出 2 代表收到
    type = Column(mysql.TINYINT, index=True)
    number = Column(String(20), index=True)
    text = Column(String(255), nullable=False)
    timestamp = Column(BigInteger, nullable=False, index=True)
    smsc = Column(String(20), nullable=False)


def get_items(db: Session, type: int, skip: int = 0, limit: int = 100):
    return db.query(Sms).filter(Sms.type == type).offset(skip).limit(limit).all()