import requests
from Cuarto import Cuarto
api = requests.get("https://api-escapamet.vercel.app")

class Pasillo(Cuarto):
    def __init__(self,cuarto):
        super().__init__(cuarto)

    pasillo = '''

                                                        _...--""|'-.
                                                _...--"         |   '-.
                                        _...--"                 |      '-.
                                _...--"                         |         '-.
                        _...--"                                 |      |'.   '-.
                _...--"          _..--¨"|                       |      |  '-.   '-.
         ...--"                 |       |                       |      |    |      |
        |                       |      ,|                _...--" '-.   |    |      |
        |                       |     []|        _...--"            '-.|   °|      |
        |                       |       |_...--"                       '.   |      |
        |                       | _...--"                                '-.|      |        
        |     |'-._       _...--"                                            '-.   |     
        |     |    |..--"                                                       '-.|
        |_...-|    |                                                       _...--""            
        '-.   |    |                                               _...--"                   
           '-.|    |                                       _...--"                              
              '-.  |                               _...--"                                       
                 '-|                       _...--"                                     
                   '-.            _...--"                              
                      '-. _...--"                
                
    Inserta R para ir a Biblioteca
    Inserta L para ir a Laboratorios
    '''

    def room(self,rooms):
        print(Pasillo.pasillo)
        rooms.append(self.name)