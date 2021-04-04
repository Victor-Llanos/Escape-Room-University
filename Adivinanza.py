from Game import Game
from Player import Player
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Adivinanza(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.question = self.juego["game"]["questions"][number]["question"]
        self.answers = self.juego["game"]["questions"][number]["answers"]
        self.clue = self.questions[number]
        self.message_requirement = self.juego["game"]["message_requirement"]

    def game(self,players):
        contraseña = "comunismonofunciona"
        print(self.requirement,"\n")
        intento = input("> ")

        if intento == contraseña and "contraseña" in players[0].inventario and not self.award in players[0].inventario:
            
            pistas = []
            pistas.append(self.clue["clue_1"])
            pistas.append(self.clue["clue_2"])
            pistas.append(self.clue["clue_3"])

            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")
            print(self.question,"\n")
            Game.pistas(players,pistas) 
            
            respuesta = input("> ")

            if respuesta in self.answers:
                print("correcto!!")
                print("Has conseguido:",self.award)
                players[0].inventario.append(self.award)
                
            else: 
                print("Incorrecto!!")
                players[0].vidas -= 0.5

        elif self.award in players[0].inventario:
            print("Ya has completado este juego")
            
        else:  
            print(self.message_requirement)

adivinanza = Adivinanza(cuarto = 0, juego = 2)
     