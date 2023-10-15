from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from endpoints import trips, user

app = FastAPI()

config = dotenv_values('.env')

@app.on_event('startup')
def connect_to_db():
    app.mongodb_client = MongoClient(config['MONGO_SRC'])
    app.database = app.mongodb_client[config['DB_NAME']]
    print('Connected to Mongo DB')

@app.on_event('shutdown')
def close_db_connection():
    app.mongodb_client.close()

app.include_router(trips.router)
app.include_router(user.router)
