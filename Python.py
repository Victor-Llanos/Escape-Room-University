from Game import Game
from Player import Player
import random
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Python(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.question = self.juego["game"]["questions"][number]["question"]
        self.answer = self.juego["game"]["questions"][number]["answer"]
        self.clue = self.questions[number]
        self.message_requirement = self.juego["game"]["message_requirement"]
 
    def game(self,players):

        if not self.award in players[0].inventario and self.requirement in players[0].inventario:
            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")
            print(self.question)


            if self.answer == "string invertido":

                pistas = []
                pistas.append(self.clue["clue_1"])
                Game.pistas(players,pistas) 

                resp = input("> ")
                frase = "oidutse ne al ortem aireinegni ed sametsis"

                if "frase" in resp:  
                    new_frase = frase[::-1]

                    if eval(resp) == new_frase:
    
                        print("Correcto!!")
                        print("Has conseguido:",self.award)
                        players[0].inventario.append(self.award)
                    
                    else: 
                        print("Incorrecto!!")
                        players[0].pistas -= 0.5
                        print("Vidas restante",players[0].vidas)

                else: 
                    print("Incorrecto!!")
                    players[0].pistas -= 0.5
                    print("Vidas restante",players[0].vidas)
            
            else:

                pistas = []
                pistas.append(self.clue["clue_1"])
                pistas.append(self.clue["clue_2"])
                pistas.append(self.clue["clue_3"]) 
                Game.pistas(players,pistas) 

                resp = input("> ")
                frase = "tengo en mi cuenta 50,00 $"
                
                if "frase" in resp:
                    
                    new_frase = int(float((frase.split()[4]).replace(",", ".")))
    
                    if eval(resp) == new_frase: 
                        print("Correcto!!")
                        print("Has conseguido:",self.award)
                        players[0].inventario.append(self.award)
                    
                    else: 
                        print("Incorrecto!!")
                        players[0].pistas -= 0.5
                        print("Vidas restante",players[0].vidas)

                else: 
                    print("Incorrecto!!")
                    players[0].pistas -= 0.5
                    print("Vidas restante",players[0].vidas)

        elif self.award in players[0].inventario:
            print("Ya has completado este juego")

        else:
            print(self.message_requirement)

python = Python(cuarto = 0, juego = 1)
