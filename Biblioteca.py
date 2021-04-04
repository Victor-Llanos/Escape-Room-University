import requests
from Cuarto import Cuarto
api = requests.get("https://api-escapamet.vercel.app")

class Biblioteca(Cuarto):
    def __init__(self,cuarto):
        super().__init__(cuarto)

    biblio = '''
         ---------------------------------------------------------------------------
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

                    Te encuentra en dormitorio... DIGO en la Biblioteca. 

        Para inspeccionar la estanteria de libros que se encuentra en el centro. Press 1
        Para inspeccionar la mueble que se encuentra a tu izquierda. Press 2
        Para inspeccionar las gabetas del mueble que se encuentra a tu derecha. Press 3

        Inserta R para ir al Saman
        Inserta L para ir a Pasillo Laboratorios
    ''' 
    def room(self,rooms):
        print(Biblioteca.biblio)
        rooms.append(self.name)
        return rooms