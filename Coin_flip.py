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


    def game(self,players):
        
        #if "carnet" in players[0].inventario and "Disco Duro" in players[0].inventario
        a = 1
        if a == 1:
            
            print("Final Boss\n")
            print("Reglas:",self.rules,"\n")

            print(graphics.boss)
            b = input("Press any key: ")

            print(graphics.boss2)
            b = input("Press any key: ")

            print(graphics.boss3)
            b = input("Press any key: ")

            print(graphics.boss4)
            b = input("Press any key: ")

            print(graphics.boss5)
            b = input("Press any key: ")


            user_guest = input("Elije Cara o Sello: ").capitalize()
            while user_guest != "Cara" and user_guest != "Sello":
                user_guest = input("Elije cara o sello: ").capitalize()

            coin = random.choice(["Cara","Sello"])
            print(coin)


            if coin == "Cara":
                print(graphics.cara,"\n")
                if user_guest == coin:
                    print("ganaste")
                else:
                    print("perdiste")
                    players[0].vidas -= 1
            else:
                print(graphics.sello,"\n")
                if user_guest == coin:
                    print("ganaste")
                else:
                    print("perdiste")
                    players[0].vidas -= 1

        else:
            print(self.message_requirement)