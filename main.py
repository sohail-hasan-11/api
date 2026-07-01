from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()

name : str | None = None
print(name)
name_annotated : Annotated[str | None, Query(max_length = 5)] = None
name_annotated = "Abdullah"
print(name_annotated)

@app.get("/name")
def print_name(name : Annotated[str | None, Query(min_length = 3, max_length = 5)] = None):
    # print(f"My name is : {name}")
    return f"My name is {name}"

# Annotated validate a parameter with first api it also check query
# print_name("Sohail")
# print_name("Abdullah Al Sourov")