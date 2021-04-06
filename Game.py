import requests
import random 

api = requests.get("https://api-escapamet.vercel.app")

class Game:
    def __init__(self,cuarto,juego):
        self.cuarto = api.json()[cuarto]
        self.juego = api.json()[cuarto]["objects"][juego]
        self.name = self.juego["game"]["name"]                      #Mutiples selfs que nos ayudaran a manejar info de la api mucho mas comodo
        self.award = self.juego["game"]["award"]                    #en las diferentes clases hijas 
        self.rules = self.juego["game"]["rules"]
        self.requirement = self.juego["game"]["requirement"]
        self.questions = self.juego["game"]["questions"]
        self.number = random.randint(0,len(self.questions)-1)
        
    def pistas(players,pistas):                                             #Metodo que se llama en los juegos que tengan pistas
        while True:                                                         #y que dependiendo de las lista de pistas en dichos juego
                opc = input("¿Quieres una pista? Y/N: ").upper()            #funcionara de uno u otra forma
                while opc != "Y" and opc != "N":
                    opc = input("Ingrese un valor valido: ").upper()

                if opc == "Y":
                    if pistas == []:
                        print("Se acabaron las pistas ;c ... Escribe tu respuesta\n")
                        break

                    elif players[0].pistas == 0:
                        print("Se te acabaron tus oportunidades de pistas\n")
                        break
                    
                    else:
                        print(pistas[0])
                        pistas.pop(0)
                        players[0].pistas -= 1
                        print("Pistas restante:",players[0].pistas)
                else:
                    print("Chic@ valiente ¿eh?\n")
                    break