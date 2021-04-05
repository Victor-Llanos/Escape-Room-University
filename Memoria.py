from Game import Game
from Player import Player
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Memoria(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)       

    def game(self,players):
        
        if self.award in players[0].inventario:
            print("Ya has completado este juego")

        else:
            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")

            print("Nota del programador: Rommel lo siento, no logre programar este juego \n pero para que el juego pueda continuar\n")
            print("Has conseguido:",self.award)
            #players[0].inventario.append(self.award)
