from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()

name : list[str] = []
name.append("Abdullah")
name.append("Sohail")
print(name)

number : list[int] = []
for i in range(1, 10):
    number.append(i)

print(number)

# name : str | None = None
# print(name)
# name_annotated : Annotated[str | None, Query(max_length = 5)] = None
# name_annotated = "Abdullah"
# print(name_annotated)

# @app.get("/name")
# def print_name(name : Annotated[str | None, Query(min_length = 3, max_length = 5)] = None):
#     # print(f"My name is : {name}")
#     return f"My name is {name}"

# Annotated validate a parameter with first api it also check query
# print_name("Sohail")
# print_name("Abdullah Al Sourov")
# print("Terminal is hot reload")
# print("After auto save terminal is do hot reload and the output in shown on terminal")
# @app.get("/")
# def number_validation(num : Annotated[list[str] | None, Query()] = None):
    # query_item = {"arr" : num}
    # # dictionary update with value and add new value
    # query_item.update({
    #     "name" : "Add new value",
    #     "arr" : num
    # })
    
    # return query_item