from pydantic import BaseModel
class authModel(BaseModel):
    name:str
    email:str
    password:int
