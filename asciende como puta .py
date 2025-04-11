
piso_actual = 1

def mover_ascensor(piso_deseado):
    global piso_actual
    if piso_deseado == piso_actual:
        print("Está en el piso: ", piso_actual)
    if piso_deseado > piso_actual:
        print("Subiendo al piso: ", piso_deseado)
        piso_actual = piso_deseado
    else:
        print("Bajando al piso: ", piso_deseado)
        piso_actual = piso_deseado

def mostrar_piso():
    print("El ascensor está en el piso :", piso_actual)

def menu():
    while True:
        print("Bienvenido al ascensor")
        print("1. Ir a un piso")
        print("2. Ver piso")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            piso_destino = int(input("Seleccione piso: "))
            mover_ascensor(piso_destino)
        elif opcion == "2":
            mostrar_piso()
        elif opcion == "3":
            print("La cagaste, dañaste el ascensor, te paso por wn")
            break

if __name__ == "__main__":
    menu()

# alooooo
