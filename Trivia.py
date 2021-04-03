from Game import Game
from Player import Player
import random
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Trivia(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.question = self.juego["game"]["questions"][number]["question"]
        self.answer = self.juego["game"]["questions"][number]
        self.clue = self.questions[number]

    def game(self,players):
        #COLOCAR CON ENQUIRIES DESPUES DEL GITCLONE
        print(self.name,"\n")
        print("Reglas:",self.rules,"\n")
        print(self.question,":")
        print("A.",self.answer["correct_answer"])
        print("B.",self.answer["answer_2"])
        print("C.",self.answer["answer_3"])
        print("D.",self.answer["answer_4"])

        pistas = []
        pistas.append(self.clue["clue_1"])

        while True:
            opc = input("¿Quieres otra una pista? Y/N: ").upper()
            while opc != "Y" and opc != "N":
                opc = input("Ingrese un valor valido: ")

            if opc == "Y":
                if pistas == []:
                    print("Se acabaron las pistas ;c ... Escribe tu respuesta")
                    break

                elif players[0].pistas == 0:
                        print("Se te acabaron tus oportunidades de pistas")

                else:
                    print(pistas[0])
                    pistas.pop(0)
                    #players[0].pistas -= 1
            else:
                print("Chic@ valiente ¿eh?")
                break

        resp = input("> ").upper()
        while resp != "A" and resp != "B" and resp != "C" and resp != "D":
            resp = input("Ves que las opciones son letras y colocas otra cosa ._. intenta de nuevo\n> ").upper()
            
        if resp == "A":
            print("Correcto!!")
            print("Has conseguido:",self.award)
            #players[0].inventario.append(self.award)
            
        else:
            print("Incorrecto!!")
            #players[0].vidas -= 0.5

trivia = Trivia(cuarto = 2, juego = 1)