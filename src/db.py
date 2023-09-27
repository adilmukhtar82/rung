from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class PyMongoDB:
    def __init__(self) :
        self.uri = "mongodb+srv://adil:thisisrung_1234@cluster0.cwrzerp.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
        self.client = MongoClient("mongodb+srv://adil:thisisrung_1234@cluster0.cwrzerp.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
        self.db = self.client["rung"]
        self.collection_games = self.db["games"]
        self.collection_players = self.db["players"]
        
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def register_player(self, name):

        self.collection_players.insert_one({"name":name})

    def record_game(self, game):
        
        self.collection_games.insert_one({"game":game})