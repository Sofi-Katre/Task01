from typing import Union

from fastapi import FastAPI

from random import randint

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def show_about():
    return {"Name": "Анна", 
            "Lastname": "Куратова", 
            "Midlename":"Евгеньевна", 
            "BDay": "24 марта 2002", 
            "Group":"Т-233902у"}

@app.get("/rnd")
def randomnumber():
    return {"Number": randint(1,10)}

@app.get("/t_square")
def calc_squire(a:int,b:int,c:int):
    p = (a + b + c) / 2
    return {"P":a+b+c, 
            "S": (p * (p - a) * (p - b) * (p - c))**(0.5)}