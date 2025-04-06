import random as r
from fastapi import FastAPI, Path, Query, HTTPException
import math
from pyd import Item

app = FastAPI()

items = [{"id": 1,
          "name": "Toster",
          'price': 100,
          "description": "This is Toster"},
         {"id": 2,
          "name": "Jeans",
          'price': 200,
          "description": "This is Jeans"},
         {"id": 3,
          "name": "iphone",
          'price': 300,
          "description": "This is Phone"},
          {"id": 4,
          "name": "Computer",
          'price': 400,
          "description": "This is PC"},
          {"id": 5,
          "name": "Mouse",
          'price': 500,
          "description": "This is Mouse"},
          {"id": 6,
          "name": "Monitore",
          'price': 600,
          "description": "This is Keyboard"}]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about_me")
def show_about_me():
    return {
        "name": "Ilya",
        "birth_date": {
            "day": 7,
            "month": "august",
            "year": 2004
        },
        "email": "ilya.nevolin.2004@mail.ru",
    }

@app.get("/rnd")
def get_random(start: int = 1, end: int = 10):
    return {
        "random integer": r.randint(start, end)
    }

@app.get("/t_square")
def get_random(a: int=Query(gt=0), b: int=Query(gt=0), c: int=Query(gt=0)):
    P = a + b + c
    p = P/2
    return {
        "perimeter": P,
        "square": math.sqrt(p*(p-a)*(p-b)*(p-c))
    }

@app.get("/items")
def get_items(name:str | None=Query(None, min_length=2),
              min_price:int | None=Query(None, gt=0),
              max_price:int | None=Query(None, gt=0),
              limit:int=Query(10, lt=100)):
    if max_price:
        if max_price < min_price:
            raise HTTPException(404, "Price min then max")
    k = []
    for item in items:
        if name:
            if name != item["name"]:
                continue
        if min_price:
            if min_price > item['price']:
                continue
        if max_price:
            if max_price < item["price"]:
                continue
        k.append(item)
    return k[:limit]

@app.get("/item/{item_id}")
def get_item(item_id:int=Path(gt=0)):
    for item in items:
        if item_id == item['id']:
            return item
    raise HTTPException(404, f"There is no such product item with id - {item_id}")

@app.post("/items")
def post_item(item: Item):
    item=dict(item)
    id = items[-1]['id'] + 1
    item["id"] = id
    items.append(item)
    return item