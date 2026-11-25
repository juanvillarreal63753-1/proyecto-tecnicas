
from menu import mostrar_menu
from ejercicios.ejercicio1 import ejecutar as ejercicio1
from ejercicios.ejercicio2 import ejecutar as ejercicio2
from ejercicios.ejercicio3 import ejecutar as ejercicio3
from ejercicios.ejercicio4 import ejecutar as ejercicio4
from ejercicios.ejercicio5 import ejecutar as ejercicio5


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
            ejercicio4()
        elif opcion == 5:
            ejercicio5()
        elif opcion == 0:
            print("\nGracias por utilizar el programa.")
            break


if __name__ == "__main__":
    main()
