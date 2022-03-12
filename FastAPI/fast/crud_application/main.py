from datetime import datetime
from typing import Optional, Text
from fastapi import FastAPI
from pydantic import BaseModel

db = []

app = FastAPI()

class Post(BaseModel):
    id: int
    name: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime
    published: Optional[bool] = False


@app.get('/blog')
def get_podts():
    return db

@app.post("/blog")
def add_post(post: Post):
    db.append(post.dict())
    return db[-1]

@app.get("/blog/{id}")
def get_post(id: int):
    post = id-1
    return db[post]

@app.post("/blog/{id}")
def update_post(id: int, post: Post):
    db[id] = post
    return {"message": "Post hes been updated succesfully"}

@app.delete("/blog/{id}")
def delete_post(id: int):
    db.pop(id-1)
    return {"message": "Post hes been delete succesfully"}
    


#/////////////////////////////////////////////////////////

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")