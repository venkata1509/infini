# from fastapi import FastAPI, Path
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# class Employee(BaseModel):
#     name: str
#     role: str
#
#
# employee = {
#     1: {
#         "name": "Nagendra",
#         "role": "Student"
#     }
# }
#
#
# # @app.get("/basic")
# # def test():
# #     return {"Test":"Manual input"}
#
# @app.get("/test/{employe_id}")
# def test(employe_id: int = Path(description="ID is required", gt=0, le=3)):
#     if employe_id in employee:
#         return employee[employe_id]
#     return {"Data": "Not found"}
#
#
# @app.get("/query/{employe_id}")
# def get_by_query(employe_id: int, name: str):
#     for employe_id in employee:
#         if employee[employe_id]["name"] == name:
#             return employee[employe_id]
#         return {"name": "Not Found"}
#     return {"Data": "Not found"}
#
#
# @app.post("/post/{employe_id}")
# def create(employe_id: int, employe: Employee):
#     if employe_id in employee:
#         return {"Employee": "ID already exsists"}
#     employee[employe_id] = employe
#     return employee[employe_id]
#
#
#
# @app.put("/update/{employe_id}")
# def update(employe_id:int, employe:Employee):
#     if employe_id not in employee:
#         return {"Employe":"NOt exsists"}
#     employee[employe_id] = employe
#
# @app.delete("/delete/{employee_id}")
# def delete_student(employee_id:int):
#     if employee_id not in employee:
#         return {"Error":"employee doesn't exists"}
#     del employee[employee_id]
#     return {"employee":"Deleted"}

# #Python3 program introducing f-string

# a=20
# print(f"my age is {a}")
# val = 'Geeks'
# print(f"{val}for{val} is a portal for {val}.")
#
#
# name = 'Om'
# age = 22
# print(f"Hello, My name is {name} and I'm {age} years old.")

# import base64
#
# credentials = "productioncoder:mypassword"
# encoded_credentials = base64.b64encode(credentials.encode()).decode()
# print(encoded_credentials)

# from typing import Annotated
#
# from fastapi import Depends, FastAPI
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
#
# app = FastAPI()
#
# security = HTTPBasic()
#
#
# @app.get("/users/me")
# def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
# return {"username": credentials.username, "password": credentials.password}