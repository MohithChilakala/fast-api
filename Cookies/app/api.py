from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'http://localhost:5500'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CooKie(BaseModel):
    key: str
    value: str

@app.post('/set-cookie')
def setCookie(cookie: CooKie, response: Response):
    response.set_cookie(cookie.key, cookie.value)
    return "Cookie added"

@app.get('/get-cookie/{key}')
def getCookie(key: str, request: Request):
    return request.cookies.get(key)