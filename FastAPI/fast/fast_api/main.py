from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")
app = FastAPI()

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request", request} )
ej = "\U0001F600"


@app.get('/blog/{id}/{name}')
def index(id : int, name : str):
    return {'data' : {id, name}}

    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)