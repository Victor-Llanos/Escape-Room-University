import requests
from Cuarto import Cuarto
api = requests.get("https://api-escapamet.vercel.app")

class Biblioteca(Cuarto):
    def __init__(self,cuarto):
        super().__init__(cuarto)

    biblio = '''
         ----------------------------------Biblio------------------------------------
        |   |                                                                   |   |
        | /||                     ______________________________                ||\ |
        || ||                    |                              |      ____     || ||
        || ||                    |       0                      |     |\____\   || ||
        || ||                    |_____/|_|\____________________|     ||    |   || ||
        || ||   ,--------,      /________________________________\    ||[--]|   || ||
        || ||   |  . . . |       |                              |     ||    |   || ||
        || ||__|`._______|`._____|______________________________|_____||[--]|___|| ||
        || /   | |________`|                                          \|____|    \ ||
        ||/     \|_________|                                                      \||
        |/_________________________________________________________________________\|

    Inserta R para ir al Saman
    Inserta L para ir a Pasillo Laboratorios
    ''' 

    def room(self,rooms):
        print(Biblioteca.biblio)
        rooms.append(self.name)