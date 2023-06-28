from fastapi import FastAPI

from controller.open_food import food_router

app = FastAPI()


@app.get("/")
async def pong():
    return {"message": "Fullstack Challenge 20201026"}


app.include_router(food_router, prefix="/food")
