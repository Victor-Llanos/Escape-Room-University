from Game import Game
from Player import Player
import random
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Logica_emoji(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        self.message_requirement = self.juego["game"]["message_requirement"]
        

    def game(self,players):

    
        if "Mensaje: Si estas gradudado puedes pisar el Samán" in players[0].inventario and "título Universitario" in players[0].inventario and not self.award in players[0].inventario: 
            number = self.number
            print(self.name,"\n")
                                                    #random para saber cual pregunta se dara 
            if number == 0:                             

                print(self.questions[number])

                while True:
                    resp = input("> ")
                    try:
                        resp = int(resp)                        
                        break
                    except ValueError:                                  
                        print("Ingrese un numero entero")                
                if resp == 67:                                      #Sabiendo ambas respuestas, solo se iguala la respuesta y alli se ve si es correcta o no

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
            print(self.message_requirement)
            players[0].vidas -= 1                   #Caso especial del juego en que no tener los requirement hace perder vida

logica_emoji = Logica_emoji(cuarto = 2, juego = 0)