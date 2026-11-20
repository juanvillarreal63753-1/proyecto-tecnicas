
from menu import mostrar_menu
from ejercicios.ejercicio1 import ejecutar as ejercicio1
from ejercicios.ejercicio2 import ejecutar as ejercicio2
from ejercicios.ejercicio3 import ejecutar as ejercicio3


def main():

    while True:

        opcion = mostrar_menu()

        if opcion == 1:
            ejercicio1()
          
        elif opcion == 2:
            ejercicio2()

        elif opcion == 3:
            ejercicio3()

        elif opcion == 4:
            print("\nEjercicio 4: Sudoku 4 x 4")
            print("Todavía estamos construyendo este ejercicio.")

        elif opcion == 5:
            print("\nEjercicio 5: Sopa de letras")
            print("Todavía estamos construyendo este ejercicio.")

        elif opcion == 0:
            print("\nGracias por utilizar el programa.")
            breakrint("\nEjercicio 2: Combinaciones")


if __name__ == "__main__":
    main()
