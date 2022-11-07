
from pymongo import MongoClient
from messageModel import messageModel
from typing import Union

DB = "fastAPIProject"
MSG_COLLECTION = "messages"

class homeClass:

 def read_root():
    return {"Hello": "World"}

 def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

 def get_status():
    """Get status of messaging server."""
    return {"status": "running"}

 def get_channels():
    """Get all channels in list form."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        distinct_channel_list = msg_collection.distinct("channel")
        return distinct_channel_list

 def get_channels():
    """Get all channels in list form."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        distinct_channel_list = msg_collection.distinct("channel")
        return distinct_channel_list

 def get_messages(channel: str):
    """Get all messages for the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        msg_list = msg_collection.find({"channel": channel})
        response_msg_list = []
        for msg in msg_list:
            response_msg_list.append(messageModel(**msg))
        return response_msg_list        

def get_channels():
    """Get all channels in list form."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        distinct_channel_list = msg_collection.distinct("channel")
        return distinct_channel_list

def get_messages(channel: str):
    """Get all messages for the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        msg_list = msg_collection.find({"channel": channel})
        response_msg_list = []
        for msg in msg_list:
            response_msg_list.append(messageModel(**msg))
        return response_msg_list

def post_message(message: messageModel):
    """Post a new message to the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        result = msg_collection.insert_one(message.dict())
        ack = result.acknowledged
        return {"insertion": ack}