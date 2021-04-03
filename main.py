from Game import Game
from Player import Player
from Mezclada import Mezclada
from Adivinanza import Adivinanza
from Logica_bool import Logica_bool
from Logica_emoji import Logica_emoji
from Criptograma import Criptograma 
from Trivia import Trivia
from Randnum import Randnum
from Python import Python

def main():

    players = []
    #Player.registrar_player(players)

    python = Python(cuarto = 0, juego = 1)
    python.game(players)

    #adivinanza = Adivinanza(cuarto = 0, juego = 2)
    #adivinanza.game(players)
           
    #criptograma = Criptograma(cuarto = 1, juego = 2)
    #criptograma.game(players)
    
    #logica_emoji = Logica_emoji(cuarto = 2, juego = 0)
    #logica_emoji.game(players)

    #trivia = Trivia(cuarto = 2, juego = 1)
    #trivia.game(players)

    #logica_bool = Logica_bool(cuarto = 3, juego = 0)
    #logica_bool.game(players)

    #mezclada = Mezclada(cuarto = 4, juego = 1)
    #mezclada.game(players)

    #randnum = Randnum(cuarto = 4, juego = 2)
    #randnum.game(players)
    
    #for i,player in enumerate(players):
    #            print("\n-----",i+1,"-----")
    #            players[0].mostrar()


main()