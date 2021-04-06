from Game import Game
import requests
#from word_search_puzzle.utils import display_panel
#from word_search_puzzle.algorithms import create_panel
api = requests.get("https://api-escapamet.vercel.app")

class Sopa(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.data = self.questions[number]


    def game(self,players):

        if "vida_sopa" in players[0].inventario:
            print("Ya has completado este juego")
        
        else:
            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")
            words = []
            respuestas = []
            words.append(self.data["answer_1"].lower())
            words.append(self.data["answer_2"].lower())
            words.append(self.data["answer_3"].lower())
            print(words)
            #result = create_panel(height=15, width=15, words_value_list=words) 
            #display_panel(result.get('panel'))     
            #Se crea la sopa de letra con una libreria especial
            #y se le pasa como palabras la lista de los nombre de la api                           

            pistas = []
            pistas.append(self.data["clue_1"])
            pistas.append(self.data["clue_2"])
            pistas.append(self.data["clue_3"])


            print("")

            while True:
                
                Game.pistas(players,pistas)
                resp = input("Ingresa la palabra que encuentre: ")
 
                if resp in respuestas:
                    print("Ya ingresaste esa palabra")

                elif resp in words and resp not in respuestas:
                    print("Correcto!!")
                    respuestas.append(resp)
                    if len(words) == len(respuestas):                  #Como en otros juego hacemos que, con la dos listas creas,
                        print("Ganaste!!")                             #creas, no de el Ganaste!!!
                        print("Has conseguido:",self.award)
                        players[0].inventario.append("vida_sopa")
                        players[0].vidas += 1
                        print("Vidas restante:",players[0].vidas)
                        break
                
                elif not resp in self.answer:
                    print("incorrecto!!")
                    players[0].vidas -= 0.5
                    print("Vidas restante:",players[0].vidas)
                    if players[0].vidas == 0 or players[0].vidas < 0:
                        break
            
sopa = Sopa(cuarto = 0, juego = 0)

