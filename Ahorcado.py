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
        self.clue = self.questions[number]

    def game(self,players):
        
        if self.award in players[0].inventario:
            print("Ya has completado este juego")

        else:
            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")
            print("Si te equivocas 6 veces Ahorcado\n")
            print(self.question,"\n")
            respuestas = []
            answer = set(self.answer.lower())

            pistas = []
            pistas.append(self.clue["clue_1"])
            pistas.append(self.clue["clue_2"])
            pistas.append(self.clue["clue_3"])
            Game.pistas(players,pistas)
            intentos = 0
            
            while True:
        
                for i in self.answer.lower():
                    
                    if i in respuestas:
                        print(i,end="")
            
                    else:
                        print("🥵",end=" ")

                resp = input("\nIngrese una letra: ")

                if len(resp) > 1 or len(resp) < 1:
                    print("Ingrese letra por letra")
                
                elif resp in respuestas:
                    print("Letra ya introducida")

                elif not resp in respuestas and resp in self.answer.lower():
                    respuestas.append(resp)
                    answer.remove(resp)
                    if answer == set():
                        print(self.answer.lower())
                        print("Ganaste!!")
                        print("Has conseguido:",self.award)
                        players[0].inventario.append(self.award)
                        break

                elif not resp in self.answer.lower():
                    print("incorrecto!!")
                    intentos += 1
                    players[0].vidas -= 0.25
                    print("Vidas restante",players[0].vidas)
                    if players[0].vidas == 0 or players[0].vidas < 0:
                        break
                    if intentos == 6:
                        print("ahorcado")
                        break

                else:
                    print("")

ahorcado = Ahorcado(cuarto = 1, juego = 0)