import requests
from Cuarto import Cuarto
api = requests.get("https://api-escapamet.vercel.app")

class Laboratorio_SL001(Cuarto):
    def __init__(self,cuarto):
        super().__init__(cuarto)

    lab = '''
         --------------------------------------Labs--------------------------------------
        |    |                                                                     |    |
        |  /||                      __________________________                     ||\  |
        | | ||                     |                          |                    || | |
        | | ||                     |  2+2 = <><               |                    || | |
        | | ||            _        |____________________---___|                    || | |
        | | ||       __  |-|__                                        _  __        || | |
        | | ||     /[[]] |_| /|                                     _| |[[]]__     || | |
        | | ||____/ ====`o  /_|____________________________________|\|_|====`o\____|| | |
        | | /    /_________/  |                                    | \_________\    \ | |
        | |/     |         |                                         |         |     \| |
        | /      |         |                                         |         |      \ |
        |/_____________________________________________________________________________\|


    Te encuentras en la cueva de sistemas (tambien conocida como labs)
    Inserta R para ir a Pasillo Laboratorios
    Inserta L para ir a Cuarto de Servidores
    ''' 

    def room(self,rooms):
        print(Laboratorio_SL001.lab)
        rooms.append(self.name)

        return rooms



    
laboratorio = Laboratorio_SL001(cuarto = 0) 