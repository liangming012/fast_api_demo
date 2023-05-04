import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from core.config import settings
from crud.crud_user import crud_user
from schemas.user import UserCreate
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
user = UserCreate(password=settings.FIRST_SUPERUSER_PASSWORD,
                  email=settings.FIRST_SUPERUSER,
                  full_name=settings.FIRST_SUPERUSER_NAME,
                  is_superuser=True)
db = SessionLocal()
crud_user.create(db, obj_in=user)
db.close()
