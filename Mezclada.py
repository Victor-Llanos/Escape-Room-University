from Game import Game
from Player import Player
import random
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Mezclada(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.question = self.juego["game"]["questions"][number]["question"]
        self.category = self.juego["game"]["questions"][number]["category"]
        self.words = self.juego["game"]["questions"][number]["words"]
        

    def game(self,players):


        if self.award in players[0].inventario:
            print("Ya has completado este juego")

        else:
            
            print(self.name)
            print("Reglas:",self.rules,"\n")
            print(self.question)
            print("Categoria:",self.category,"\n")

            for i in self.words:
                self.desordenar = random.sample(i, len(i))
                self.palabra = ''.join(self.desordenar)
                print(">",self.palabra,"\n")

            respuesta = []

            for i in self.words:
                
                while True:
                    resp = input("> ")
                    if resp in self.words:
                        if resp in respuesta:
                            print("Ya se respondio")
                        else:
                            respuesta.append(resp)
                            print(respuesta)

                            if len(respuesta) == len(self.words):
                                print("\nJuego completado\n") 
                                print(self.award,":comunismonofunciona")
                                players[0].inventario.append(self.award)
                            break
                    else:
                        print("incorrecto")
                        players[0].vidas -= 0.5
                    
mezclada = Mezclada(cuarto = 4, juego = 1)
