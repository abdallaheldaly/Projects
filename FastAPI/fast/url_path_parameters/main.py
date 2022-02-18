from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": Data  }

ej = "\U0001F600"

Data = [
    {
        'id':1,
        'name':'Abdallah',
        'phone':'123436t',
    },
    {
        'id':2,
        'name':'Mohammad',
        'phone':'56786586',
    },
    {
        'id':3,
        'name':'Daly',
        'phone':'3242354345',
    },
]

@app.get("/api/{api_id}", status_code=200)
def fetch_api(api_id:int)-> dict:
    
    result = [new_data for new_data in Data if new_data['id']==api_id]

    if result:
        return result[0]

#/////////////////////////////////////////////////////////

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")