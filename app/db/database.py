from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import init_db, db

init_db()

SQLALCHEMY_DATABASE_URL: str = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    db['mysql_username'],
    db['mysql_password'],
    db['mysql_host'],
    db['mysql_port'],
    db['mysql_database'])

# 初始化数据库连接:
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()