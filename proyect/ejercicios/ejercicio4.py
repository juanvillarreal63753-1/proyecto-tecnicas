import random


def es_valido(tablero, fila, col, num):
    # Revisar fila
    if num in tablero[fila]:
        return False

    # Revisar columna
    for f in range(4):
        if tablero[f][col] == num:
            return False

    # Revisar bloque 2x2
    inicio_fila = (fila // 2) * 2
    inicio_col = (col // 2) * 2
    for f in range(inicio_fila, inicio_fila + 2):
        for c in range(inicio_col, inicio_col + 2):
            if tablero[f][c] == num:
                return False

    return True


def imprimir_tablero(tablero):
    borde = "+-----+-----+"
    print(borde)
    for f in range(4):
        fila_str = "|"
        for c in range(4):
            val = tablero[f][c]
            simbolo = "." if val == 0 else str(val)
            fila_str += f" {simbolo}"
            if c == 1:
                fila_str += " |"
        fila_str += " |"
        print(fila_str)
        if f == 1:
            print(borde)
    print(borde)


def generar_tablero_inicial(cantidad):
    tablero = [[0 for _ in range(4)] for _ in range(4)]
    posiciones = [(f, c) for f in range(4) for c in range(4)]
    random.shuffle(posiciones)

    colocados = 0
    for fila, col in posiciones:
        if colocados == cantidad:
            break
        numeros = [1, 2, 3, 4]
        random.shuffle(numeros)
        for num in numeros:
            if es_valido(tablero, fila, col, num):
                tablero[fila][col] = num
                colocados += 1
                break

    return tablero


def resolver_sudoku(tablero):
    contador = [0]

    def backtrack():
        for fila in range(4):
            for col in range(4):
                if tablero[fila][col] == 0:
                    for num in range(1, 5):
                        contador[0] += 1
                        if es_valido(tablero, fila, col, num):
                            tablero[fila][col] = num
                            if backtrack():
                                return True
                            tablero[fila][col] = 0
                    return False
        return True

    resuelto = backtrack()
    return resuelto, contador[0]


def pedir_cantidad_inicial():
    while True:
        try:
            n = int(input("¿Cuántas casillas llenas al inicio (4 a 10)? "))
            if 4 <= n <= 10:
                return n
            print("Error: debe ingresar un número entre 4 y 10.")
        except ValueError:
            print("Error: ingrese un número entero válido.")


def ejecutar():
    print("\n--- Sudoku 4 x 4 ---")
    cantidad = pedir_cantidad_inicial()

    while True:
        tablero_inicial = generar_tablero_inicial(cantidad)
        tablero_trabajo = [fila[:] for fila in tablero_inicial]

        print("Tablero inicial (generado al azar):")
        imprimir_tablero(tablero_inicial)

        print("Resolviendo...")
        resuelto, valores_probados = resolver_sudoku(tablero_trabajo)

        if resuelto:
            print(f"Tablero resuelto. Valores probados: {valores_probados}")
            imprimir_tablero(tablero_trabajo)
            break
        else:
            print("Este tablero respeta las reglas, pero no tiene solución.")
            opcion = input("¿Desea generar otro tablero? (s/n): ").strip().lower()
            if opcion not in ("s", "si", "sí"):
                break


if __name__ == "__main__":
    ejecutar()