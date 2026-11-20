
def ejecutar():
    print("\n--- Paréntesis balanceados ---")

    while True:
        try:
            n = int(input("Ingrese n (1 a 8): "))

            if 1 <= n <= 8:
                break

            print("Error: n debe estar entre 1 y 8.")

        except ValueError:
            print("Error: ingrese un número entero.")

    print(f"\nEmpiezo con una cadena vacía.")
    print(f"Tengo {n} paréntesis '(' y {n} paréntesis ')' para ubicar.")

    resultados = []

    def generar(cadena, abiertos, cerrados):

        # Caso base: ya ubicamos todos los paréntesis
        if abiertos == n and cerrados == n:
            resultados.append("".join(cadena))
            return

        # Elegir un paréntesis de apertura
        if abiertos < n:
            cadena.append("(")

            # Explorar
            generar(cadena, abiertos + 1, cerrados)

            # Deshacer
            cadena.pop()

        # Elegir un paréntesis de cierre
        if cerrados < abiertos:
            cadena.append(")")

            # Explorar
            generar(cadena, abiertos, cerrados + 1)

            # Deshacer
            cadena.pop()

    generar([], 0, 0)

    print(f"\nCadenas balanceadas ({len(resultados)}):")

    for resultado in resultados:
        print(resultado)


if __name__ == "__main__":
    ejecutar()
