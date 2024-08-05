# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app=FastAPI()
#
# # @app.get("/",description="This your first route")
# # def root():
# #     return {"Message":"Hello"}
# #
# # @app.post("/")
# # def post():
# #     return {"Message":"Hello from the post route"}
#
# @app.put("/")
# def put():
#    return {"Message":"Hello from the put route "}

from typing import Optional
from models import Base, User
from pydantic import BaseModel
from schema import userschema
from database import engine,Sessionlocal
from sqlalchemy.orm import Session
from fastapi import FastAPI,Depends
Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()



@app.post("/adduser")
def add_user(request:userschema, db: Session = Depends(get_db)):
    user = User(name=request.name, email = request.email,nickname=request.nickname)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/user/{user_name}")
def get_users(user_name,db: Session= Depends(get_db)):
    users = db.query(User).filter(User.name == user_name).first()
    return users
