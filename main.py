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
from Ahorcado import Ahorcado
#from Sopa import Sopa
from Cuarto import Cuarto
from Laboratorio_SL001 import Laboratorio_SL001
from Biblioteca import Biblioteca
from Plaza import Plaza
from Pasillo import Pasillo
from Servidores import Servidores
from Start_game import Start_game
import collections

def escapamet(rooms,players):

    while True:
        
        biblio = Biblioteca(cuarto = 1) 
        biblio.room(rooms)
        print(rooms)
        cuenta1 = collections.Counter(rooms)
        print(cuenta1)
            
        opc = input("> ").upper()
        while opc != "R" and opc != "L" and opc != "1" and opc != "2" and opc != "3":
            opc = input("Ingreso invalido, intente de nuevo: ").upper()

        if opc == "R":

            plaza= Plaza(cuarto = 2) 
            plaza.room(rooms)
            print(rooms)
            cuenta1 = collections.Counter(rooms)
            print(cuenta1)
            opc = input("> ").upper()
            while opc != "L" and opc != "1" and opc != "2" and opc != "3":
                opc = input("Ingreso invalido, intente de nuevo: ").upper()

            if opc == "L":
                pass

            elif opc == "1":
                logica_emoji = Logica_emoji(cuarto = 2, juego = 0)
                logica_emoji.game(players)
                if players[0].vidas == 0:
                    print("endgame")
                    break
                
            elif opc == "2":
                trivia = Trivia(cuarto = 2, juego = 1)
                trivia.game(players)
                if players[0].vidas == 0:
                    print("endgame")
                    break
            else:
                pass

        elif opc == "L":
                
            while True:
                
                pasillo = Pasillo(cuarto = 3) 
                pasillo.room(rooms)
                print(rooms)
                cuenta1 = collections.Counter(rooms)
                print(cuenta1)
                opc = input("> ").upper()
                while opc != "R" and opc != "L" and opc != "1":
                    opc = input("Ingreso invalido, intente de nuevo: ").upper()

                if opc == "R":
                    break

                elif opc == "L":

                    while True:

                        laboratorio = Laboratorio_SL001(cuarto = 0) 
                        laboratorio.room(rooms)
                        print(rooms)
                        cuenta1 = collections.Counter(rooms)
                        print(cuenta1)
                        opc = input("> ").upper()
                        while opc != "R" and opc != "L" and opc != "1" and opc != "2" and opc != "3":
                            opc = input("Ingreso invalido, intente de nuevo: ").upper()
                            
                        if opc == "R":
                            break
                            
                        elif opc == "L":

                            while True:

                                servidores= Servidores(cuarto = 4) 
                                servidores.room(rooms)
                                print(rooms)
                                cuenta1 = collections.Counter(rooms)
                                print(cuenta1)
                                opc = input("> ").upper()
                                while opc != "R" and opc != "1" and opc != "2" and opc != "3":
                                    opc = input("Ingreso invalido, intente de nuevo: ").upper()
                                    
                                if opc == "R":
                                    break

                                elif opc == "1":
                                    pass

                                elif opc == "2":
                                    mezclada = Mezclada(cuarto = 4, juego = 1)
                                    mezclada.game(players)

                                else:
                                    randnum = Randnum(cuarto = 4, juego = 2)
                                    randnum.game(players)

                        elif opc == "1":
                            pass

                        elif opc == "2":
                            python = Python(cuarto = 0, juego = 1)
                            python.game(players)

                        else:
                            adivinanza = Adivinanza(cuarto = 0, juego = 2)
                            adivinanza.game(players)
                        
                else:
                    logica_bool = Logica_bool(cuarto = 3, juego = 0)
                    logica_bool.game(players)

        elif opc == "1":
            ahorcado = Ahorcado(cuarto = 1, juego = 0)
            ahorcado.game(players)
            
        elif opc == "2":
            pass
            
        else:
            criptograma = Criptograma(cuarto = 1, juego = 2)
            criptograma.game(players)

    return rooms,players

def main():

    #rooms = []
    players = []
    Player.registrar_player(players)
    #escapamet(rooms,players)
    #cuenta1 = collections.Counter(rooms)
 

    #while True:
    #    if players[0].vidas > 0:
    #        Start_game.escapamet(rooms,players)


    #CUARTOS

    #laboratorio = Laboratorio_SL001(cuarto = 0) 
    #laboratorio.room(rooms)

    #biblio = Biblioteca(cuarto = 1) 
    #biblio.room(rooms)
    
    #plaza= Plaza(cuarto = 2) 
    #plaza.room(rooms)

    #pasillo= Pasillo(cuarto = 3) 
    #pasillo.room(rooms)

    #servidores= Servidores(cuarto = 4) 
    #servidores.room(rooms)

    #cuenta1 = collections.Counter(rooms)
    #print(cuenta1)

    #JUEGOS

    #sopa = Sopa(cuarto = 0, juego = 0)
    #sopa.game(players)

    #python = Python(cuarto = 0, juego = 1)
    #python.game(players)

    #adivinanza = Adivinanza(cuarto = 0, juego = 2)
    #adivinanza.game(players)
           
    ahorcado = Ahorcado(cuarto = 1, juego = 0)
    ahorcado.game(players)

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