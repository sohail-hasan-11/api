from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated
# app = FastAPI()

# name : str | None = None

# def print_name(name : str | None = None):
#     print(f"My name is = {name}")
# print_name()
# print_name("Abdullah")

# class person(BaseModel):
#     name : str 
#     age : int
#     address : str 

# def print_inf(p : person):
#     print(f"Name is {p.name} age {p.age} address {p.address}")

# print_inf(person("name" : "Sohail", "age" : 10, "address" : "Dhaka"))
# print_inf({"Abdullah", 25, "Kurigram"})

# class codeforces(BaseModel):
#     handle : str
#     rating : int | None

# @app.post("/register")
# def codeforces_user(user : codeforces):
#     return{
#         "user" : user,
#         "docs" : f"User has post something and I get the information on user calss that  I can be processed"
#     }


# @app.get("/")
# def func() :
#     return "Alhamdulillah first api learn"

# @app.get("/home")
# def obj():
#     return {
#         "name" : "Abdullah",
#         "age" : 25,
#         "cgp" : 3.1
#     }
# @app.get("/user/{user_id}")
# def get_user(user_id : int):
#     return{
#         "name" : f"Hello user id {user_id}",
#         "user" : user_id,
#     }
# @app.get("/item")
# def get_user(name : str, price : int):
#     return{
#         "name" : name,
#         "price" : price,
#         "massege" : f"product {name}'s prize is {price}"
#     }

