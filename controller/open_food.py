from typing import Optional

from fastapi import APIRouter, HTTPException
from fastapi import Query

from repository.handler_db import MongoPipeline

food_router = APIRouter()

repository = MongoPipeline()


@food_router.get("", status_code=200)
def get_foods(page_size: Optional[int] = Query(10, gt=0)):
    response = repository.get_foods(page_size)
    if not response:
        raise HTTPException(status_code=404, detail="Item not found")
    return repository.get_foods(page_size)


@food_router.get("/{code}", status_code=200)
def get_foods(code: str):
    response = repository.get_food(code)
    if not response:
        raise HTTPException(status_code=404, detail="Barcode not found")
    return repository.get_food(code)
