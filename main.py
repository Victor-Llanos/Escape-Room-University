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
from Laboratorio_SL001 import Laboratorio_SL001
from Biblioteca import Biblioteca
from Plaza import Plaza
from Pasillo import Pasillo
from Servidores import Servidores
import collections


def main():

    players = []
    rooms = []
    cuenta1 = collections.Counter(rooms)

    Player.registrar_player(players)
        
    while True:

        biblio = Biblioteca(cuarto = 1) 
        biblio.room(rooms)
        print(rooms)
        opc = input("> ").upper()
        while opc != "R" and opc != "L" and opc != "1" and opc != "2" and opc != "3":
            opc = input("Ingreso invalido, intente de nuevo: ").upper()

        if opc == "R":

            plaza= Plaza(cuarto = 2) 
            plaza.room(rooms)
            print(rooms)
            while opc != "L" and opc != "1" and opc != "2" and opc != "3":
                opc = input("Ingreso invalido, intente de nuevo: ").upper()

            if opc == "L":
                pass

            elif opc == "1":
                pass
            elif opc == "2":
                pass
            else:
                pass

        elif opc == "L":
            
            while True:
            
                pasillo = Pasillo(cuarto = 3) 
                pasillo.room(rooms)
                print(rooms)
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
                                    pass

                        elif opc == "1":
                            pass

                        elif opc == "2":
                            pass

                        else:
                            adivinanza = Adivinanza(cuarto = 0, juego = 2)
                            adivinanza.game(players)
                    
                else:
                    pass

        elif opc == "1":
            pass
        
        elif opc == "2":
            pass
        
        else:
            pass


    #Player.registrar_player(players)

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

    #python = Python(cuarto = 0, juego = 1)
    #python.game(players)

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