from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'http://localhost:5500'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Product(BaseModel):
    name: str
    description: str | None = None
    price: float = Field(gt=10)
    quantity: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "quantity": 5,
                }
            ]
        }
    }


products = []


@app.get('/')
def home():
    return "Hello"


@app.get('/products')
def getItems():
    return products


@app.post('/item')
def addItem(product: Product, response_model=Product):
    products.append(product)
    return products[-1]
