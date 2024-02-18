from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'http://localhost:5500'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {'message': 'hello world'}


@app.get('/item/{item}')
def getItem(item: str, page: int = 1):
    return 'These are ' + item + 's from page ' + str(page)

@app.get('/items')
def getItem(page: Annotated[int, Query(alias="page-no", max_length = 50)] = 10):
    return "Items from page " + str(page)