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

    def game(self,players):
        contraseña = "comunismonofunciona"
        print(self.requirement,"\n")
        intento = input("> ")

        if intento == contraseña:
            pistas = []
            pistas.append(self.clue["clue_1"])
            pistas.append(self.clue["clue_2"])
            pistas.append(self.clue["clue_3"])

            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")
            print(self.question,"\n")
            
            while True:
                opc = input("¿Quieres una pista? Y/N: ").upper()
                while opc != "Y" and opc != "N":
                    opc = input("Ingrese un valor valido: ")

                if opc == "Y":
                    if pistas == []:
                        print("Se acabaron las pistas ;c ... Escribe tu respuesta")
                        break

                    elif players[0].pistas == 0:
                        print("Se te acabaron tus oportunidades de pistas")
                        break
                    
                    else:
                        print(pistas[0])
                        pistas.pop(0)
                        #players[0].pistas -= 1
                else:
                    print("Chic@ valiente ¿eh?")
                    break

            respuesta = input("> ")

            if respuesta in self.answers:
                print("correcto!!")
                print("Has conseguido:",self.award)
                #players[0].inventario.append(self.award)
                
            else: 
                print("Incorrecto!!")
                #players[0].vidas -= 0.5

        else:  
            print(api.json()[0]["objects"][2]["game"]["message_requirement"])

adivinanza = Adivinanza(cuarto = 0, juego = 2)
     