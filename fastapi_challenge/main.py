from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the request body with name, studying, and age/hobbies
class AboutMe(BaseModel):
    name: str
    study: str
    hobbies: str
    
# Define a POST endpoint that receives Intern details and returns them

users = []

@app.post("/users")
async def post_user(text: AboutMe):
    for user in users:
        if text.name == user.name:
            raise HTTPException(status_code=403, detail=f"{text.name} is already in the database")
    
    users.append(text);
    return text

@app.get("/users")
async def get_users():
    return users