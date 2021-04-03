import requests
import random 

api = requests.get("https://api-escapamet.vercel.app")

class Game:
    def __init__(self,cuarto,juego):
        self.cuarto = api.json()[cuarto]
        self.juego = api.json()[cuarto]["objects"][juego]
        self.name = self.juego["game"]["name"]
        self.award = self.juego["game"]["award"]
        self.rules = self.juego["game"]["rules"]
        self.requirement = self.juego["game"]["requirement"]
        self.questions = self.juego["game"]["questions"]
        self.number = random.randint(0,len(self.questions)-1)
        