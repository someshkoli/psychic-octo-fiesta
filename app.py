from fastapi import FastAPI

app = FastAPI()

@app.get("/recomm")
async def get_recommendation(x: int):
    return x*x

@app.get("/shivika")
async def get_recommendation():
    return "shivika"


