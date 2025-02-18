from fastapi import FastAPI
from math_functions import add

app = FastAPI()

@app.get("/")
async def root(first_number: int, second_number: int):
    answer = add(first_number, second_number)
    return {"message": "Hello World", "value": str(answer)}

@app.get("/health")
async def healthCheck(apiResponse):
    if apiResponse == True:
        answer = "API status is good"
    else:
        answer = "API status is not good"

    return {"message": answer}