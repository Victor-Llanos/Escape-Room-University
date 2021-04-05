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

            Ten encuentras en sala de servidores... Si solo es una sala de servidores

        Para inspeccionar la puerta que se encuentra en el centro. Press 1
        Para inspeccionar los racks que se encuentra a tu izquierda. Press 2
        Para inspeccionar la papelera que se encuentra a tu derecha. Press 3
        
        Inserta R para ir a Laboratorios
                
    ''' 
    def room(self,rooms):
        print(Servidores.servidores)
        rooms.append(self.name)
        return rooms