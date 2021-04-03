from Game import Game
from Player import Player
import requests
import random

api = requests.get("https://api-escapamet.vercel.app")

class Criptograma(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.question = self.juego["game"]["questions"][number]["question"]
        self.desplazamiento = self.juego["game"]["questions"][number]["desplazamiento"]

    def game(self,players):
        #ARREGLA LAS LETRAS ACENTUADAS
        llave = True 
        #if "llave" in players[0].inventario:
        if llave:
        
            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")
            
            frase = self.question

            if self.desplazamiento == 2:
                des2 = frase.maketrans("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ", "cdefghijklmnñopqrstuvwxyzabCDEFGHIJKLMNÑOPQRSTUVWXYZABcgkqwCGKQW")
                frase = frase.translate(des2)
                print(frase)
                print('''
                    +-------------------+-------------------+
                    | c d e f g h i j k | a b c d e f g h i |
                    | l m n ñ o p q r s | j k l m n ñ o p q |
                    | t u v w x y z a b | r s t u v w x y z |
                    +-------------------+-------------------+
                    ''')

            elif self.desplazamiento == 4:
                des4 = des4 = frase.maketrans("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ", "efghijklmnñopqrstuvwxyzabcdEFGHIJKLMNÑOPQRSTUVWXYZABCDeimsyEIMSY")
                frase = frase.translate(des4)
                print(frase)
                print('''
                +-------------------+-------------------+
                | e f g h i j k l m | a b c d e f g h i |
                | n ñ o p q r s t u | j k l m n ñ o p q |
                | v w x y z a b c d | r s t u v w x y z |
                +-------------------+-------------------+
                ''')
    
            else:
                des5 = frase.maketrans("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ", "fghijklmnñopqrstuvwxyzabcdeFGHIJKLMNÑOPQRSTUVWXYZABCDEfjntzFJNTZ")
                frase = frase.translate(des5)
                print(frase)
                print('''
                +-------------------+-------------------+
                | f g h i j k l m n | a b c d e f g h i |
                | ñ o p q r s t u v | j k l m n ñ o p q |
                | w x y z a b c d e | r s t u v w x y z |
                +-------------------+-------------------+
                ''')

            new_frase = self.question
            a,b =  'áéíóúüÁÉÍÓÚÜ','aeiouuAEIOUU'
            trans = str.maketrans(a,b)
            new_frase.translate(trans)

            resp = input("> ")

            if resp == new_frase.translate(trans):
                print("correcto!!")
                print("Has conseguido:",self.award)
                #players[0].inventario.append(self.award)

            else:
                print("incorrecto!!")
                #players[0].vidas -= 1 

        if not llave:
            print(api.json()[1]["objects"][2]["game"]["message_requirement"])

criptograma = Criptograma(cuarto = 1, juego = 2)