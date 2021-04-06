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
from Memoria import Memoria
from Mate import Mate
from Laboratorio_SL001 import Laboratorio_SL001
from Biblioteca import Biblioteca
from Plaza import Plaza
from Pasillo import Pasillo
from Servidores import Servidores
import collections
import graphics
import time 

def registrar_player(players):

    user = input("Ingrese su username: ")
    while (len(user) < 6) or (len(user) > 12):                        
        user = input("El username tiene que ser de entre 6 a 12 caracteres: ")  
        
    with open("Database_Players.txt") as dbe:
        datos = dbe.readlines()

    for dato in datos:
                
        player1 = dato[:-1].split("//")
        if player1[0] == user:
            print("Usuario ya registrado.")
            return main()

        else:
            pass


    password = input("Ingrese su contraseña: ")
    while (len(password) < 8):
        password = input("La contraseña tiene que ser mayor a 8 caracteres: ")

    while True:
        age = input("Ingrese su edad: ")
        try:
            age = int(age)
            break
        except ValueError:
            print("Ingrese un numero entero: ")

    inventario = ["Ganas de vivir"] 
    #Al empezar el juego tienes en tu invetario "ganas de vivir" que me sirve                          
    #me sirve como recuerdo para decirme que si puedo con este proyecto... creo

    avatares = ["Scharifker", "Eugenio Mendoza", "Pelusa", "Gandhi", "Camaron"]     
    #Ademas de los avatares dados por el doc, se agrega a camaron
    #inspirado en el constate recuerdo que me siento mal en la silla
    #teniendo la postura camaron
    for i, avatar in enumerate(avatares, 1):                                        
        print(i, avatar)                                                 

    while True:
        opc = input("Ingrese el numero correspondiente al avatar: ")
        try:
            opc = int(opc)
            break
        except ValueError:
            print("Ingrese un numero entero: ")
                    
    selc = avatares[opc-1]  
    avatar = selc

    dificultad = input("Introduzca la dificultad a jugar:\n1. Facil\n2. Media\n3. Dificil\n>> ")
    while dificultad != "1" and dificultad != "2" and dificultad != "3":
        dificultad = input("Ingreso invalido, intente de nuevo: ")
            

    if dificultad == "1":
        print("Nuevo? o es que tienes miedo?\n")            #dependiendo de la dificultad seleccion se le dara un numero de vidas y pistas 
        dificultad = "Facil"                                   
        vidas = 5.0                                                                  
        pistas = 5
        player = Player(user,password,age,avatar,dificultad,vidas,pistas,inventario)
        with open("Database_Players.txt","a+") as dbe:
            dbe.write(f"{user}//{password}//{age}//{avatar}//{dificultad}//{vidas}//{pistas}\n")
        players.append(player)
        player.mostrar()
        print(graphics.narr1)
        return players

    elif dificultad == "2":
        print("Esta bien para comenzar.\n")
        dificultad = "Media"
        vidas = 3.0
        pistas = 3
        player = Player(user,password,age,avatar,dificultad,vidas,pistas, inventario)
        with open("Database_Players.txt","a+") as dbe:
            dbe.write(f"{user}//{password}//{age}//{avatar}//{dificultad}//{vidas}//{pistas}\n")
        players.append(player)
        player.mostrar()
        print(graphics.narr1)
        return players

    else:
        print("Pues anda, que tenemos un valiente. Suerte... La necesitaras.\n")
        dificultad = "Dificil"
        vidas = 1.0
        pistas = 2
        player = Player(user,password,age,avatar,dificultad,vidas,pistas, inventario)
        with open("Database_Players.txt","a+") as dbe:
            dbe.write(f"{user}//{password}//{age}//{avatar}//{dificultad}//{vidas}//{pistas}\n")
        players.append(player)
        player.mostrar()
        print(graphics.narr1)
        return players

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
                    memoria = Memoria(cuarto = 2, juego = 2)
                    memoria.game(players)

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
                                        coin_flip = Coin_flip(cuarto = 4, juego = 0)
                                        coin_flip.game(players)
                                        if "Parar el cronómetro y ganar el juego" in players[0].inventario:
                                            print(graphics.win)
                                            return main()
                                        
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
            
        elif opc == "1":
            ahorcado = Ahorcado(cuarto = 1, juego = 0)
            ahorcado.game(players)
            
            
        elif opc == "2":
            mate = Mate(cuarto = 1, juego = 1)
            mate.game(players)
            
        else:
            criptograma = Criptograma(cuarto = 1, juego = 2)
            criptograma.game(players)
            
    print(graphics.muerte)
    return rooms,players

def main():

    rooms = []
    players = []
    
    time_limit = 5
    start_time = time.time()

    while True:
        print(graphics.menu)
        selc = input("> ")
        while selc != "1" and selc != "2" and selc != "3" and selc != "4" and selc != "5" and selc != "6":
            selc = input("Ingreso invalido, intente de nuevo: ")

        if selc == "1":
            registrar_player(players)
            escapamet(rooms,players)
            del players[0]
     
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

    #mate = Mate(cuarto = 1, juego = 1)
    #mate.game(players)

    #criptograma = Criptograma(cuarto = 1, juego = 2)
    #criptograma.game(players)
    
    #logica_emoji = Logica_emoji(cuarto = 2, juego = 0)
    #logica_emoji.game(players)

    #trivia = Trivia(cuarto = 2, juego = 1)
    #trivia.game(players)

    #memoria = Memoria(cuarto = 2, juego = 2)
    #memoria.game(players)

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