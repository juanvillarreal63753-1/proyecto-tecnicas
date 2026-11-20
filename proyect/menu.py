
def mostrar_menu():
    print("\n" + "=" * 50)
    print("   PROYECTO BACKTRACKING - Técnicas de Programación")
    print("=" * 50)

    print("1. Cadenas binarias sin dos 1 seguidos")
    print("2. Combinaciones: elegir k de n")
    print("3. Paréntesis balanceados")
    print("4. Sudoku 4 x 4")
    print("5. Sopa de letras")
    print("0. Salir")

    while True:
        try:
            opcion = int(input("\nElija una opción: "))

            if opcion >= 0 and opcion <= 5:
                return opcion
            else:
                print("Error: elija una opción entre 0 y 5.")

        except ValueError:
            print("Error: debe ingresar un número entero.")
