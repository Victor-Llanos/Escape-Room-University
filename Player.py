class Player:
    def __init__(self, user, password, age, avatar, dificultad, vidas, pistas, inventario):
        self.user = user
        self.password = password
        self.age = age
        self.avatar = avatar
        self.dificultad = dificultad
        self.vidas = vidas
        self.pistas = pistas
        self.inventario = inventario
        
    def mostrar(self):
        print(f"Usuario: {self.user}\nPassword: {self.password}\nEdad: {self.age}\nAvatar: {self.avatar}\nDificultad: {self.dificultad}\nVidas: {self.vidas}\nPistas: {self.pistas}\nInventario:{self.inventario}\n")

    def registrar_player(players):

        user = input("Ingrese su username: ")
        while (len(user) < 6) or (len(user) > 12):
            user = input("El username tiene que ser de entre 6 a 12 caracteres: ")  

        #if user in .txt:
        #   confirmacion = print("Username ya en uso, ingrese otro username") 
        #    if confirmacion in .txt:
        #   break

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
            
        avatares = ["Scharifker", "Eugenio Mendoza", "Pelusa", "Gandhi", "Camaron"]
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
            print("Nuevo? o es que tienes miedo?\n")
            dificultad = "Facil"
            vidas = 5.0
            pistas = 5
            player = Player(user,password,age,avatar,dificultad,vidas,pistas,inventario)
            players.append(player)
            player.mostrar()
            return players

        elif dificultad == "2":
            print("Esta bien para comenzar.\n")
            dificultad = "Media"
            vidas = 3.0
            pistas = 3
            player = Player(user,password,age,avatar,dificultad,vidas,pistas, inventario)
            players.append(player)
            player.mostrar()
            return players

        else:
            print("Pues anda, que tenemos un valiente. Suerte... La necesitaras.\n")
            dificultad = "Dificil"
            vidas = 1.0
            pistas = 2
            player = Player(user,password,age,avatar,dificultad,vidas,pistas, inventario)
            players.append(player)
            player.mostrar()
            return players