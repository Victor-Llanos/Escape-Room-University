from Game import Game
from Player import Player
import random
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Randnum(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        
    def game(self,players):

        if self.award in players[0].inventario:
            print("Ya has completado este juego")

        else:
        
            ans = random.randint(1,15)
            print(self.name)
            print("Reglas:",self.rules,"\n")
            print(ans)

            while True:
                print(self.question,"\n")
                while True:
                    resp = input("> ")
                    try:
                        resp = int(resp)
                        break
                    except ValueError:
                        print("Ingrese un numero entero: ")

                if resp == ans:
                    print("Correcto!!")
                    print("Has conseguido:",self.award)
                    #players[0].inventario.append(self.award)
                    break

                elif resp < ans:
                    print("Incorrecto!!")
                    opc = input("¿Quieres una pista? Y/N: ").upper()
                    while opc != "Y" and opc != "N":
                        opc = input("Ingrese un valor valido: ")

                    if opc == "Y":
                        print("pista: el numero es mayor")
                    else:
                        print("Chic@ valiente ¿eh?")

                elif resp > ans:
                    print("Incorrecto!!")
                    opc = input("¿Quieres una pista? Y/N: ").upper()
                    while opc != "Y" and opc != "N":
                        opc = input("Ingrese un valor valido: ")

                    if opc == "Y":
                        print("pista: el numero es menor")
                    else:
                        print("Chic@ valiente ¿eh?")

randnum = Randnum(cuarto = 4, juego = 2)