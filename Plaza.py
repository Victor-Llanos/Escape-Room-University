import requests
from Cuarto import Cuarto
api = requests.get("https://api-escapamet.vercel.app")

class Plaza(Cuarto):
    def __init__(self,cuarto):
        super().__init__(cuarto)

    saman = '''
                                                               ; ; ;
                                        ;  ;                ;          ;
                                    ;          ;        ;                 ;;
                           ;  ;  ;              ;   ;;                 .        ;
                        ;                         ;         .         ;  
                    ;        .              .               ;%     ;;         ;
                               ,           ,                 :;%  %;   
                                :         ;                   :;%;'     .,   ;
                  ;    ,.        %;     %;            ;        %;'    ,;       ;
                ;        ;       ;%;  %%;        ,     %;    ;%;    ,%'
                ;         %;       %;%;      ,  ;       %;  ;%;   ,%;'         ;
                 ;         ;%;      %;        ;%;        % ;%;  ,%;'          ;
                ;           `%;.     ;%;     %;'         `;%%;.%;'           ;
              ;               `:;%.    ;%%. %@;        %; ;@%;%'        
                                `:%;.  :;bd%;          %;@%;'           ;
                 ;             ;; `@%:.  :;%.         ;@@%;'         ;;
                            ;       `@%.  `;@%.      ;@@%;         ;
                    ;   ;             `@%%. `@%%    ;@@%;        ;
                                        ;@%. :@%%  %@@%;       
                          ;            ;  %@bd%%%bd%%:;    ; ; ;
                            ;     ;; ;      #@%%%%%:;;   ;
                               ; ;           \@bd%d/
                                    __...---  d%b%%  --...__
                             _...--"   .-'    :@%%:   ' -.  ""--..__
                           -"    ' .  . '     @@%;'  '  . .  '      ""--..__  
                  _...--"  .  '-  '    .--'   @%%%%     .  '  . '  _________""--..__
         _...--"                    ' ..      @%;%D              /_________/|
                            .  '  .       _.- %%;.% -._  .  '  . | |      | |
                 _________              .'    @%%.-    '.        |/       |/
                |\________\  -'   ' .   '.   `-._.-    .'  '  - .               -
                | |      | |   ' '        '-._______.-'     '  .   .   -      ._
                 \|       \|          .      ~,                     _
                                .       .        .    ' '-.      .-         -      .  

                
            Ten encuentras en el bello saman (No te montes en las ramas por favor)

        Para inspeccionar el saman que se encuentra en el centro. Press 1
        Para inspeccionar el banco que se encuentra a tu izquierda. Press 2
        Para inspeccionar el banco que se encuentra a tu derecha. Press 3
            
        
        Inserta L para ir a Biblioteca
    '''
    def room(self,rooms):
        print(Plaza.saman)
        rooms.append(self.name)
        return rooms