from fastapi import FastAPI
from db import PyMongoDB
from typing import Dict
app = FastAPI()
client_db = PyMongoDB()
from pydantic import BaseModel

class Team (BaseModel):
    p1 : str
    p2: str
    win: int

class Game(BaseModel):
    date: str
    t1: Dict[str, Team]
    t2: Dict[str, Team]
    total_games: int



@app.get('/')
async def home():
    return {"RUNG": "Game is on."}

@app.post('/player/{name}')
async def register_player(player: str):
    try:
        client_db.register_player(player)
        return {"status":"successful"}
    except:
        return {"status":"not successful"}
    
@app.post('/record_game/')
async def record_game(game: Game):
    db_game = {}
    db_game['date'] = game.date
    db_game['t1'] = game.t1.values()
    db_game['t2'] = game.t2.values()
    db_game['total_games'] = game.total_games

    dict_game = game.dict()
    client_db.record_game(dict_game)
    
