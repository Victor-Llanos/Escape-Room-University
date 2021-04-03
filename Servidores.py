import requests
from Cuarto import Cuarto
api = requests.get("https://api-escapamet.vercel.app")

class Servidores(Cuarto):
    def __init__(self,cuarto):
        super().__init__(cuarto)

    servidores = '''
                                                        _...--""|'-.
                                                _...--"         |   '-.
                                        _...--"                 |      '-.
                                _...--"                         |         '-.
                        _...--"          _..--"|                |      |'.   '-.
                _...--"                 |      |            (_) |      |  '-.   '-.
         ...--"            _.-'-.       |      |[]          |#| |      |    |      |
        |        _.-'-.   |'-._.-"|     |     °|         _..\ /" '-.   |    |      |
        |       |'-._.-"| |  |_.-"|     |      | _...--"            '-.|   °|      |
        |       |  |_.-"| |  |_.-"|     |_...--"                       '.   |      |
        |       |  |_.-"| |  |_.-"|_..-"                                 '-.|      | 
        |       |  |_.-"|_|  |_.-"|                                          '-.   |     
        |       |  |_.-"| '-.|_.-"                                              '-.|
        |_...--"'-.|_.-"                                                   _...--""            
        '-.                                                        _...--"                   
           '-.                                             _...--"                              
              '-.                                  _...--"                                       
                 '-.                       _...--"                                     
                    '-.            _...--"                              
                       '-. _...--"                

    Inserta R para ir a Laboratorios
                
    ''' 
    def room(self,rooms):
        print(Servidores.servidores)
        rooms.append(self.name)