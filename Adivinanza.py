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
        contraseña = "comunismonofunciona" #establezco la contraseña, que le se muestra al jugador al ganar en palabra mezclafa
        print(self.requirement,"\n")
        intento = input("> ")
        
        if intento == contraseña and "contraseña" in players[0].inventario and not self.award in players[0].inventario: #se hace la validacion necesario para ingresar al juego 
            
            pistas = []
            pistas.append(self.clue["clue_1"])      #Se hace una lista y se apedean cuantas pistas tenga el juego
            pistas.append(self.clue["clue_2"])      #para luego usar un metodo que toma la lista 
            pistas.append(self.clue["clue_3"])

            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")
            print(self.question,"\n")
            Game.pistas(players,pistas) 
            
            respuesta = input("> ")
            while not respuesta.isalpha():
                respuesta = input("Use solo letras")

            if respuesta in self.answers:                   #Si la respuesta del usuario se encuentra en la lista de 
                print("correcto!!")                         #de la api dara correcto y otorgara el award
                print("Has conseguido:",self.award)
                players[0].inventario.append(self.award)
                
            else: 
                print("Incorrecto!!")           #Caso contrario, perdera vida y a su vez se le mostrara cuanto le queda
                players[0].vidas -= 0.5
                print("Vidas restante",players[0].vidas)

        elif self.award in players[0].inventario:      #Validacion que se asegura que solo pueda jugar una vez, si tiene el premio 
            print("Ya has completado este juego")      #no puede volver a jugar
            
        else:                                   
            print(self.message_requirement)

adivinanza = Adivinanza(cuarto = 0, juego = 2)
     