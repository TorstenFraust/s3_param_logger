from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

items = [] # TODO: how to pre-fill this with data?


class Item(BaseModel):
    text: str
    is_done: bool = False

    
@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items", response_model=list[Item])
def get_items(limit: int = 10, skip: int = 0):
    return items[skip : skip + limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id <0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    item = items[item_id]
    return item