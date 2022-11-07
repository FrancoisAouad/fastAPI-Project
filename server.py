from fastapi import FastAPI,Request,Response
from fastapi.testclient import TestClient
from auth import authClass
authService =authClass()

app = FastAPI()


# @app.get("/")
# authClass().read_root()

# @app.get("/items/{item_id}")

