from Game import Game
from Player import Player
import random
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Randnum(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.question = self.juego["game"]["questions"][number]["question"]
        
    def game(self,players):

        if self.award in players[0].inventario:
            print("Ya has completado este juego")

        else:    #Se crea un contador para saber cuando llegue a 3 quitarle la vida correspondiente

            errores = 0

            ans = random.randint(1,15)
            print(self.name)
            print("Reglas:",self.rules,"\n")
            print(ans)

            while True:
                print(self.question,"\n")
                while True:
                    resp = int(input("> "))
                    try:
                        resp = int(resp)
                        break
                    except ValueError:
                        print("Ingrese un numero entero: ")

                if resp == ans:
                    print("Correcto!!")
                    print("Has conseguido:",self.award)
                    players[0].inventario.append(self.award)
                    break

                elif resp < ans:
                    print("Incorrecto!!")
                    errores += 1
                    if errores == 3:                                  #Cuando se llegue al 3 en el contador, se vuelve a reiniciar para seguir 
                        errores = 0                                   #el ciclo
                        players[0].vidas -= 0.25
                        print("Vidas restante:",players[0].vidas)
                        if players[0].vidas == 0 or players[0].vidas < 0:
                            break

                    opc = input("¿Quieres una pista? Y/N: ").upper()
                    while opc != "Y" and opc != "N":
                        opc = input("Ingrese un valor valido: ")

                    if opc == "Y":

                        if players[0].pistas == 0:
                            print("Se te acabaron tus oportunidades de pistas\n")

                        else:
                            print("pista: el numero es menor")
                            players[0].pistas -= 1
                            print("Pistas restante:",players[0].pistas)

                    else:
                        print("Chic@ valiente ¿eh?")

                elif resp > ans:
                    print("Incorrecto!!")
                    errores += 1
                    if errores == 3:
                        errores = 0
                        players[0].vidas -= 0.25
                        print("Vidas restante:",players[0].vidas)
                        if players[0].vidas == 0 or players[0].vidas < 0:
                            break

                    opc = input("¿Quieres una pista? Y/N: ").upper()
                    while opc != "Y" and opc != "N":
                        opc = input("Ingrese un valor valido: ")

                    if opc == "Y":

                        if players[0].pistas == 0:
                            print("Se te acabaron tus oportunidades de pistas\n")

                        else:
                            print("pista: el numero es mayor")
                            players[0].pistas -= 1
                            print("Pistas restante:",players[0].pistas)
                            
                    else:
                        print("Chic@ valiente ¿eh?")

randnum = Randnum(cuarto = 4, juego = 2)