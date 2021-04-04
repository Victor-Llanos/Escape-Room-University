from Game import Game
from Player import Player
import requests
from word_search_puzzle.utils import display_panel
from word_search_puzzle.algorithms import create_panel
api = requests.get("https://api-escapamet.vercel.app")

class Sopa(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.answer = self.questions[number]

    def game(self,players):

        #if self.award in players[0].inventario:
        #    print("Ya has completado este juego")
        
        #else:
        print(self.name,"\n")
        print("Reglas:",self.rules,"\n")
        words = []
        respuestas = []
        words.append(self.answer["answer_1"].lower())
        words.append(self.answer["answer_2"].lower())
        words.append(self.answer["answer_3"].lower())
        print(words)
        result = create_panel(height=15, width=15, words_value_list=words)
        display_panel(result.get('panel'))

        print("")

        while True:

            resp = input("Ingresa la palabra que encuentre: ")
        
            if resp in respuestas:
                print("Ya ingresaste esa palabra")

            elif resp in words and resp not in respuestas:
                print("Correcto!!")
                respuestas.append(resp)
                if len(words) == len(respuestas):
                    print("Ganaste!!")
                    print("Has conseguido:",self.award)
                    #players[0].inventario.append(self.award)
                    break

            elif len(words) == len(respuestas):
                print("Ganaste!!")
                print("Has conseguido:",self.award)
                #players[0].inventario.append(self.award)
                break
            
            elif not resp in self.answer:
                print("incorrecto!!")
                #players[0].vidas -= 0.5
            

sopa = Sopa(cuarto = 0, juego = 0)
