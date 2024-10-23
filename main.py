from registro import menu
from registro import creacion
from registro import inasistencias
from registro import bonos
# from cash import bonos
# from cash import calculo_nomina


while True:

    print("""
        Bienvenido a ACME SAS

        Porfavor escoja una de la siguientes opcciones
        """)
    menu()
    opc = input(" => ")

    if opc == "1":
        creacion()
    elif opc == "2":
         inasistencias()
    elif opc == "3":
        bonos()
    # elif opc == "4":
    #     buscar()
    # elif opc == "5":
    #     historico()
    # elif opc == "6":
    #     reporte()    
    # elif opc == "7":
    #     historico()