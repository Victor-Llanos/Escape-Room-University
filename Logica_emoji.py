from Game import Game
from Player import Player
import random
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Logica_emoji(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        #number = self.number
        #self.question = self.juego["game"]["questions"][number]
        

    def game(self,players):

    
        if "Mensaje: Si estas gradudado puedes pisar el Samán" in players[0].inventario and "título Universitario" in players[0].inventario and not self.award in players[0].inventario: 
            number = self.number
            print(self.name,"\n")
            #print("Reglas:",self.rules,"\n")

            if number == 0:

                print(self.questions[number])

                while True:
                    resp = input("> ")
                    try:
                        resp = int(resp)
                        break
                    except ValueError:
                        print("Ingrese un numero entero")                
                if resp == 67:

                    print("Correcto!!")
                    print("Has conseguido:",self.award)
                    players[0].inventario.append(self.award)

                else:
                    print("Incorrecto!!")
                    players[0].vidas -= 1
                    print("Vidas restante",players[0].vidas)
                    
            else:
                print(self.questions[number]) 

                while True:
                    resp = input("> ")
                    try:
                        resp = int(resp)
                        break
                    except ValueError:
                        print("Ingrese un numero entero")  

                if resp == 41:
                    print("Correcto!!")
                    print("Has conseguido:",self.award)
                    players[0].inventario.append(self.award)
                
                else:
                    print("Incorrecto!!")
                    players[0].vidas -= 1
                    print("Vidas restante",players[0].vidas)

        elif self.award in players[0].inventario:
            print("Ya has completado este juego")

        else:
            print(api.json()[2]["objects"][0]["game"]["message_requirement"])
            players[0].vidas -= 1

logica_emoji = Logica_emoji(cuarto = 2, juego = 0)