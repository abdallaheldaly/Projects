from typing import Optional
from fastapi import FastAPI

app = FastAPI()

Data = [
    {
        'id':1,
        'name':'Abdallah',
        'phone':'1234363',
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
# Uniform Resource Locator

# http://server/path/program?query_string

@app.get("/search/", status_code=200)
def search(
    keyword: Optional[str] = None, max_results: Optional[int] = None
)->dict:
    
    if not keyword:
        return{"results": Data[:max_results]}

    results = filter(lambda recipe: keyword.lower() in recipe["name"].lower(), Data)
    return{"results": list(results)[:max_results]}


#/////////////////////////////////////////////////////////

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")