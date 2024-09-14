from typing import Optional
from fastapi import FastAPI
from dataclasses import dataclass

app = FastAPI()


@app.get("/greet")
def greet(username: Optional[str] = "User"):
    return {"status": "ok", "message": f"Hello {username}"}


@app.get("/greet/{username}")
def greet_by_name(username: str):
    return {"status": "ok", "message": f"Hello {username}"}


from pydantic import BaseModel
class User(BaseModel):
    name : str
    age : int
    
@app.post("/create-user")
def create_user(user_data:User):
    print(user_data)
    return {"status": "ok", "message": f"Hello {user_data}"}
    
