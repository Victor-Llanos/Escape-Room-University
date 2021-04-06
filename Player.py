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
    #Se usa un metedo que luego retornara todos los datos del usuario en la lista de main


        
        