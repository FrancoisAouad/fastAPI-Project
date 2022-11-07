from pymongo import MongoClient
client = MongoClient(host='127.0.0.1', port=27017)

DB = "fastApiProject"
AUTH_COLLECTION = "auth"