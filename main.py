from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()

name : str | None = None
print(name)


# For auto reload the main file
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


