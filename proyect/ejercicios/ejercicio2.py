
def ejecutar():
    print("\n--- Combinaciones: elegir k de n ---")

    while True:
        try:
            n = int(input("Ingrese n (1 a 12): "))
            k = int(input("Ingrese k: "))

            if 1 <= k <= n <= 12:
                break

            print("Error: debe cumplirse 1 <= k <= n <= 12.")

        except ValueError:
            print("Error: ingrese números enteros.")

    numeros = list(range(1, n + 1))

    print(f"\nNúmeros disponibles: {numeros}")
    print(f"Empiezo con un grupo vacío y debo elegir {k} números.")

    combinaciones = []
    llamadas = 0

    def generar(inicio, grupo):
        nonlocal llamadas
        llamadas += 1

        # Caso base: ya elegimos k números
        if len(grupo) == k:
            combinaciones.append(grupo.copy())
            return

        # Elegir el siguiente número
        for i in range(inicio, n + 1):

            grupo.append(i)

            # Explorar
            generar(i + 1, grupo)

            # Deshacer
            grupo.pop()

    generar(1, [])

    print(f"\nGrupos ({len(combinaciones)}):")

    for combinacion in combinaciones:
        print(combinacion)

    print(f"\nLlamadas a la función recursiva: {llamadas}")


if __name__ == "__main__":
    ejecutar()
