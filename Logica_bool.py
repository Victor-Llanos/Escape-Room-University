from Game import Game
from Player import Player
import random
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Logica_bool(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.question = self.juego["game"]["questions"][number]["question"]
        self.answer = self.juego["game"]["questions"][number]["answer"]
        self.message_requirement = self.juego["game"]["message_requirement"]

    def game(self,players):
        #martillo" in players[0].inventario and
        if "martillo" in players[0].inventario and not "vida_bool" in players[0].inventario:
            
            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")

            print(self.question)
            resp = input("> ")

            if resp == self.answer:
                print("Correcto!!")
                print("Has conseguido:",self.award)
                players[0].inventario.append("vida_bool")
                players[0].vidas += 1
            else:
                print("Incorrecto!!")
                players[0].vidas -= 0.5
                print("Vidas restante",players[0].vidas)

        elif self.award in players[0].inventario:
            print("Ya has completado este juego")
                
        else:
            print(self.message_requirement)

logica_bool = Logica_bool(cuarto = 3, juego = 0)