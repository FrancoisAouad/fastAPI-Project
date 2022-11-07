from pydantic import BaseModel

class messageModel(BaseModel):
    channel: str
    author: str
    text: str