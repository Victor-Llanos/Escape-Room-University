from Game import Game
from Player import Player
import random
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Mezclada(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.question = self.juego["game"]["questions"][number]["question"]
        self.category = self.juego["game"]["questions"][number]["category"]
        self.words = self.juego["game"]["questions"][number]["words"]
        

    def game(self,players):


        if self.award in players[0].inventario:
            print("Ya has completado este juego")

        else:
            
            print(self.name)
            print("Reglas:",self.rules,"\n")
            print(self.question)
            print("Categoria:",self.category,"\n")

            for i in self.words:
                self.desordenar = random.sample(i, len(i))      #Se usa la .sample para desordenar las letra asegurando que desordene la misma cantidad 
                self.palabra = ''.join(self.desordenar)         #de letras que tiene la palabra, para luego unir la palabra (eso con cada palabra) 
                print(">",self.palabra,"\n")

            respuesta = []

            for i in self.words:
                
                while True:
                    resp = input("> ")
                    if resp in self.words:                      #Se va recorriendo si la respuesta esta en la lista de la api para luego agregarla a una lista
                        if resp in respuesta:                   #lista que se usara para acabar el juego si tiene la misma tamaño en palabra que la de la api
                            print("Ya se respondio")            #ignorando la palabras repetidas
                        else:
                            respuesta.append(resp)
                            print(respuesta)

                            if len(respuesta) == len(self.words):
                                print("\nJuego completado\n") 
                                print(self.award,":comunismonofunciona")        #Se hace printa del award como del la contraseña en si, que en otro juego 
                                players[0].inventario.append(self.award)        #tendra que tipear por consola
                            break
                    else:
                        print("incorrecto")
                        players[0].vidas -= 0.5
                        print("Vidas restante: ",players[0].vidas)
                    
mezclada = Mezclada(cuarto = 4, juego = 1)
