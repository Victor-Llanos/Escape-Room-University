from Game import Game
from Player import Player
import requests
import random

api = requests.get("https://api-escapamet.vercel.app")

class Ahorcado(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.question = self.juego["game"]["questions"][number]["question"]
        self.answer = self.juego["game"]["questions"][number]["answer"]

    def game(self,players):
        
        #if self.award in players[0].inventario:
        #    print("Ya has completado este juego")

        print(self.name,"\n")
        print("Reglas:",self.rules,"\n")
        print(self.question)
        cambio = "🥵 " * len(self.answer) 
        print(cambio)

        respuestas = []

        while True:
            resp = input("> ")

            if len(resp) > 1 or len(resp) < 1:
                print("No ingrese mas de una letras hasta terminar el juego") 
            
            elif resp in self.answer:
                respuestas.append(resp)
                print(respuestas)

                if resp in respuestas:
                    print("Ya usaste esa letra")

            else:
                print("incorrecto")


        
ahorcado = Ahorcado(cuarto = 1, juego = 0)