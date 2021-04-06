from Game import Game
from Player import Player
import requests
import random
import graphics

api = requests.get("https://api-escapamet.vercel.app")

class Coin_flip(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        self.message_requirement = self.juego["game"]["message_requirement"]
        self.name = "Final Boss"

    def game(self,players):
        
        if "carnet" in players[0].inventario and "Disco Duro" in players[0].inventario:
            
            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")

            print(graphics.boss)                  #a manera que ayude la narrativa el boss va
            b = input("Press any key: ")          #haciendo su monologo que fue indiscretamente
                                                  #tomado del personaje sans del juego undertale
            print(graphics.boss2)                 #esto porque me hace feliz y no creo que no afecta a la narrativa
            b = input("Press any key: ")

            print(graphics.boss3)
            b = input("Press any key: ")

            print(graphics.boss4)
            b = input("Press any key: ")

            print(graphics.boss5)
            b = input("Press any key: ")

            print(graphics.boss6)
            b = input("Press any key: ")

            print(graphics.boss7)
            b = input("Press any key: ")

            while True:
                user_guest = input("Elije Cara o Sello: ").capitalize()
                while user_guest != "Cara" and user_guest != "Sello":
                    user_guest = input("Elije cara o sello: ").capitalize()

                coin = random.choice(["Cara","Sello"])
                print(coin)

                if coin == "Cara":                    #Se asegura de saber si en random es cara o sello 
                    print(graphics.cara,"\n")         #de alli se ve si erro o acerto y se hcae print de la moneda
                    if user_guest == coin:
                        print("ganaste")
                        players[0].inventario.append(self.award)
                        break
                    else:
                        print("perdiste")
                        players[0].vidas -= 1
                        print("Vidas restante:",players[0].vidas)
                        if players[0].vidas == 0 or players[0].vidas < 0:
                            break
                else:
                    print(graphics.sello,"\n")
                    if user_guest == coin:
                        print("ganaste")
                        players[0].inventario.append(self.award)
                        break
                    else:
                        print("perdiste")
                        players[0].vidas -= 1
                        print("Vidas restante:",players[0].vidas)
                        if players[0].vidas == 0 or players[0].vidas < 0:
                            break

        #else:
            #print(self.message_requirement)