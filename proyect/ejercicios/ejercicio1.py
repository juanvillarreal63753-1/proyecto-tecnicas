
def ejecutar():
    print("\n--- Cadenas binarias sin dos 1 seguidos ---")

    while True:
        try:
            n = int(input("Ingrese n (1 a 15): "))

            if 1 <= n <= 15:
                break

            print("Error: n debe estar entre 1 y 15.")

        except ValueError:
            print("Error: ingrese un número entero.")

    print(f"\nTrabajo con cadenas de longitud {n}.")
    print("Empiezo con una cadena vacía.")

    cadenas = []

    def generar(cadena):
        if len(cadena) == n:
            cadenas.append("".join(cadena))
            return

        for bit in ["0", "1"]:

            # Descartar dos unos consecutivos
            if bit == "1" and cadena and cadena[-1] == "1":
                continue

            # Elegir
            cadena.append(bit)

            # Explorar
            generar(cadena)

            # Deshacer
            cadena.pop()

    generar([])

    print(f"\nCadenas válidas ({len(cadenas)}):")
    print(" ".join(cadenas))


if __name__ == "__main__":
    ejecutar()
