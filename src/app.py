from fastapi import FastAPI
from db import PyMongoDB
from typing import Dict
from pydantic import BaseModel

app = FastAPI()
client_db = PyMongoDB()


# define base model for the team
class Team (BaseModel):
    p1 : str
    p2: str
    win: int

# define base model for the game, i.e., date, t1 (dict), t2 (dict), total games
class Game(BaseModel):
    date: str
    t1: Dict[str, Team]
    t2: Dict[str, Team]
    total_games: int


# home page
@app.get('/')
async def home():
    return {"RUNG": "Game is on."}

#post reqeust from the client to register the player
@app.post('/player/{name}')
async def register_player(player: str):
    try:
        client_db.register_player(player)
        return {"status":"successful"}
    except:
        return {"status":"not successful"}

# post request from the client for recording the game   
@app.post('/record_game/')
async def record_game(game: Game):

    #convert param object to dictionary
    dict_game = game.dict()

    #insert game
    client_db.record_game(dict_game)
    
