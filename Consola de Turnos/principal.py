import numeros

def principal():
    while True:
        print("¿A que área deser dirigirse?\n[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmetica\n")
        try:
            opcion = input("Elija su opcion: ").upper()
            ["P", "F", "C"].index(opcion)
        except ValueError:
            print("Esa no es una opcion válida")
        else:
            break
    numeros.decorar_numero(opcion)

def inicio():
    while True:
        principal()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]\n").upper()
            ['S', 'N'].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()
