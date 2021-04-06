from Game import Game
import requests
import graphics

api = requests.get("https://api-escapamet.vercel.app")

class Mate(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)  
        self.message_requirement = self.juego["game"]["message_requirement"]

    def game(self,players):
        
        if "libro de matemáticas" in players[0].inventario:
            
            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")

            print(graphics.mate)

            print("Nota del programador: Rommel... lo siento, no logre programar este juego \n pero para que el juego pueda continuar\n")
            print("Has conseguido:",self.award)
            players[0].inventario.append("Vida_mate")
            players[0].vidas += 1

        else:
            print(self.message_requirement)

