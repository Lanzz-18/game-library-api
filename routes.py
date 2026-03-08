from fastapi import APIRouter
from models import Game
from database import games_collection
from bson import ObjectId

router = APIRouter()

@router.get("/games")
def get_games():
    games = list(games_collection.find())
    for game in games:
        game["_id"] = str(game["_id"])
    return games

@router.post("/games")
def add_game(game: Game):
    new_game = dict(game)
    result = games_collection.insert_one(new_game)
    new_game["_id"] = str(result.inserted_id)
    return new_game

@router.delete("/games/{id}")
def delete_game(id: str):
    games_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "game deleted"}

@router.put("/games/{id}")
def update_game(id: str, game: Game):
    games_collection.update_one({"_id": ObjectId(id)}, {"$set": dict(game)})
    return {"message":"Game updated"}