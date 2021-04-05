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
from Sopa import Sopa
from Coin_flip import Coin_flip
from Cuarto import Cuarto
from Laboratorio_SL001 import Laboratorio_SL001
from Biblioteca import Biblioteca
from Plaza import Plaza
from Pasillo import Pasillo
from Servidores import Servidores
import collections
import graphics

def escapamet(rooms,players):

    while players[0].vidas > 0:
        
        biblio = Biblioteca(cuarto = 1) 
        biblio.room(rooms)
        print(rooms)
        cuenta1 = collections.Counter(rooms)
        print(cuenta1)
            
        opc = input("> ").upper()
        while opc != "R" and opc != "L" and opc != "1" and opc != "2" and opc != "3":
            opc = input("Ingreso invalido, intente de nuevo: ").upper()

        if opc == "R":

            while players[0].vidas > 0:

                plaza= Plaza(cuarto = 2) 
                plaza.room(rooms)
                print(rooms)
                cuenta1 = collections.Counter(rooms)
                print(cuenta1)
                opc = input("> ").upper()
                while opc != "L" and opc != "1" and opc != "2" and opc != "3":
                    opc = input("Ingreso invalido, intente de nuevo: ").upper()

                if opc == "L":
                    break

                elif opc == "1":
                    logica_emoji = Logica_emoji(cuarto = 2, juego = 0)
                    logica_emoji.game(players)
                    
                elif opc == "2":
                    trivia = Trivia(cuarto = 2, juego = 1)
                    trivia.game(players)
                    
                else:
                    pass

        elif opc == "L":
                
            while players[0].vidas > 0:
                
                pasillo = Pasillo(cuarto = 3) 
                pasillo.room(rooms,players)
                print(rooms)
                cuenta1 = collections.Counter(rooms)
                print(cuenta1)
                opc = input("> ").upper()
                while opc != "R" and opc != "L" and opc != "1":
                    opc = input("Ingreso invalido, intente de nuevo: ").upper()

                if opc == "R":
                    break

                elif opc == "L":
                    
                    if "martillo" in players[0].inventario:

                        while players[0].vidas > 0:

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

                                while players[0].vidas > 0:

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
                                sopa = Sopa(cuarto = 0, juego = 0)
                                sopa.game(players)
                                pass
                            elif opc == "2":
                                python = Python(cuarto = 0, juego = 1)
                                python.game(players)

                            else:
                                adivinanza = Adivinanza(cuarto = 0, juego = 2)
                                adivinanza.game(players)
                        
                    else:
                        print("La puerta esta blooqueada, tengo que buscar algo para abrirla")
                        pass          
                else:
                    logica_bool = Logica_bool(cuarto = 3, juego = 0)
                    logica_bool.game(players)
                    if players[0].vidas == 0:
                        print(graphics.muerte)
                        exit(0)

        elif opc == "1":
            ahorcado = Ahorcado(cuarto = 1, juego = 0)
            ahorcado.game(players)
            
            
        elif opc == "2":
            pass
            
        else:
            criptograma = Criptograma(cuarto = 1, juego = 2)
            criptograma.game(players)
            
    print(graphics.muerte)
    return rooms,players

def main():

    rooms = []
    players = []

    while True:
        print(graphics.menu)
        selc = input("> ")
        while selc != "1" and selc != "2" and selc != "3" and selc != "4" and selc != "5" and selc != "6":
            selc = input("Ingreso invalido, intente de nuevo: ")

        if selc == "1":
            Player.registrar_player(players)
            escapamet(rooms,players)

        elif selc == "2":
            pass
        
        elif selc == "3":
            pass
        
        elif selc == "4":
            pass

        elif selc == "5":
            break

        else:
            pass

    #cuenta1 = collections.Counter(rooms)
 

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
           
    #ahorcado = Ahorcado(cuarto = 1, juego = 0)
    #ahorcado.game(players)

    #criptograma = Criptograma(cuarto = 1, juego = 2)
    #criptograma.game(players)
    
    #logica_emoji = Logica_emoji(cuarto = 2, juego = 0)
    #logica_emoji.game(players)

    #trivia = Trivia(cuarto = 2, juego = 1)
    #trivia.game(players)

    #logica_bool = Logica_bool(cuarto = 3, juego = 0)
    #logica_bool.game(players)

    #coin_flip = Coin_flip(cuarto = 4, juego = 0)
    #coin_flip.game(players)

    #mezclada = Mezclada(cuarto = 4, juego = 1)
    #mezclada.game(players)

    #randnum = Randnum(cuarto = 4, juego = 2)
    #randnum.game(players)
    
    #for i,player in enumerate(players):
    #            print("\n-----",i+1,"-----")
    #            players[0].mostrar()


main()