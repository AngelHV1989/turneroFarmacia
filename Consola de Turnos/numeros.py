
def numero_perfumeria():
    for n in range(1, 50000):
        yield f"P - {n}"


def numero_farmacia():
    for n in range(1, 50000):
        yield f"F - {n}"


def numero_cosmeticos():
    for n in range(1, 50000):
        yield f"C - {n}"

p = numero_perfumeria()
f = numero_perfumeria()
c = numero_farmacia()

def decorar_numero(opcion):
    print('\n' + '*' * 23)
    print("Su numero es:")
    if opcion == "P":
        print(next(p))
    elif opcion == "F":
        print(next(f))
    else:
        print(next(c))
    print("Espere a ser atendido")
    print('\n' + '*' * 23 + "\n")