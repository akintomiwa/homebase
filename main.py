# main.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
# from databases import Database
# from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

# # using local db 
# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
# SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


# using Azure 
# Update DATABASE_URL with your Azure Database for PostgreSQL connection details
# DATABASE_URL = os.getenv(
#     "DATABASE_URL",
#     "postgresql://username:password@your-postgres-server-url:5432/your-database",
# )

# engine = create_engine(DATABASE_URL)
# database = Database(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    hashed_password = Column(String)

# FastAPI setup
app = FastAPI()

# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Token Authentication
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_user(db: Session, username: str):
#     return db.query(User).filter(User.username == username).first()

# Routes
# @app.post("/token")
# async def login(form_data: OAuth2PasswordBearer = Depends()):
#     db = SessionLocal()
#     user = get_user(db, form_data.username)
#     if not user or not verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return {"access_token": user.username, "token_type": "bearer"}

# # Protected Route
# @app.get("/protected")
# async def protected_route(current_user: str = Depends(oauth2_scheme)):
#     return {"message": "Hello, {}".format(current_user)}


# Active Routes 

@app.get("/")
async def root():
    return {"message":"Hello World"}


# Example endpoint providing information about your website/projects
@app.get("/website_info")
def get_website_info():
    return {
        "name": "Your Name",
        "bio": "Your bio or description",
        "projects": [
            {"name": "Project 1", "description": "Description of Project 1"},
            {"name": "Project 2", "description": "Description of Project 2"},
        ],
    }