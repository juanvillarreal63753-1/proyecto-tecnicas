from pathlib import Path

DIRECCIONES = [
    (-1, 0),  # Arriba
    (1, 0),   # Abajo
    (0, -1),  # Izquierda
    (0, 1),   # Derecha
]


def obtener_ruta_sopa():
    # Busca sopa.txt en proyect/datos/sopa.txt respecto a este archivo
    base_dir = Path(__file__).resolve().parent.parent
    ruta = base_dir / "datos" / "sopa.txt"
    if not ruta.exists():
        ruta = Path("sopa.txt")
    return ruta


def cargar_sopa(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = [linea.strip().upper() for linea in archivo if linea.strip()]

    if len(lineas) != 10:
        raise ValueError(f"Se esperaban 10 filas en sopa.txt, se encontraron {len(lineas)}.")

    cuadricula = []
    for linea in lineas:
        # Soporta filas separadas por espacios o filas de 10 caracteres pegados
        partes = linea.split()
        if len(partes) == 10:
            fila = partes
        elif len(linea) == 10:
            fila = list(linea)
        else:
            raise ValueError(f"Fila inválida en sopa.txt: '{linea}'")
        cuadricula.append(fila)

    return cuadricula


def mostrar_cuadricula(cuadricula):
    print("    " + " ".join(str(c) for c in range(1, 11)))
    for f in range(10):
        print(f"{f + 1:2d}  " + " ".join(cuadricula[f]))


def pedir_palabra():
    while True:
        palabra = input("Palabra a buscar: ").strip().upper()
        if palabra and palabra.isalpha():
            return palabra
        print("Error: ingrese una palabra no vacía con solo letras.")


def dibujar_recorrido(cuadricula, palabra, camino):
    # camino es una lista de tuplas (fila_0idx, col_0idx)
    print(f"\nRecorrido de {palabra}:")
    print("     " + " ".join(str(c) for c in range(1, 11)))
    print("    +" + "-" * 21 + "+")

    for f in range(10):
        # Construimos una grilla de 19 columnas horizontales para conectar con '-'
        # Índices pares (0, 2, ..., 18) corresponden a las columnas 1..10
        celdas = ["." for _ in range(10)]
        conexiones_h = [" " for _ in range(9)]

        for idx, (cf, cc) in enumerate(camino):
            if cf == f:
                celdas[cc] = palabra[idx]
            # Conexión horizontal entre casillas consecutivas en la misma fila
            if idx + 1 < len(camino):
                nf, nc = camino[idx + 1]
                if cf == f and nf == f and abs(nc - cc) == 1:
                    col_izq = min(cc, nc)
                    conexiones_h[col_izq] = "-"

        fila_visual = celdas[0]
        for c in range(1, 10):
            fila_visual += conexiones_h[c - 1] + celdas[c]

        print(f"{f + 1:2d}  | {fila_visual} |")

        # Conexión vertical '|' hacia la fila siguiente
        if f < 9:
            conexiones_v = [" " for _ in range(10)]
            for idx in range(len(camino) - 1):
                f1, c1 = camino[idx]
                f2, c2 = camino[idx + 1]
                if abs(f2 - f1) == 1 and c1 == c2:
                    if f1 == f and f2 == f + 1:
                        conexiones_v[c1] = "|"
                    elif f2 == f and f1 == f + 1:
                        conexiones_v[c1] = "|"
            print("    | " + " ".join(conexiones_v) + " |")

    print("    +" + "-" * 21 + "+")
    inicio = (camino[0][0] + 1, camino[0][1] + 1)
    fin = (camino[-1][0] + 1, camino[-1][1] + 1)
    print(f"Inicio: {inicio}  Fin: {fin}")


def buscar_palabra(cuadricula, palabra):
    pasos = [0]
    visitado = [[False for _ in range(10)] for _ in range(10)]
    camino = []

    def backtrack(fila, col, indice):
        # Descartar: fuera de límites, ya visitada o letra no coincide
        if not (0 <= fila < 10 and 0 <= col < 10):
            return False
        if visitado[fila][col]:
            return False
        if cuadricula[fila][col] != palabra[indice]:
            return False

        # Elegir
        visitado[fila][col] = True
        camino.append((fila, col))
        pasos[0] += 1
        actual_str = "".join(palabra[: indice + 1])
        print(f"Paso {pasos[0]}: '{palabra[indice]}' en ({fila + 1},{col + 1}) camino: {actual_str}")

        # Caso base: palabra completa encontrada
        if indice == len(palabra) - 1:
            return True

        # Explorar vecinos ortogonales (arriba, abajo, izquierda, derecha)
        for df, dc in DIRECCIONES:
            if backtrack(fila + df, col + dc, indice + 1):
                return True

        # Deshacer: ninguna vecina llevó a completar la palabra
        visitado[fila][col] = False
        camino.pop()
        pasos[0] += 1
        print(f"Paso {pasos[0]}: retrocedo, ({fila + 1},{col + 1}) no lleva a '{palabra[indice + 1]}'")
        return False

    for f in range(10):
        for c in range(10):
            if cuadricula[f][c] == palabra[0]:
                pasos[0] += 1
                print(f"Paso {pasos[0]}: empiezo en ({f + 1},{c + 1}) con '{palabra[0]}'")
                if backtrack(f, c, 0):
                    return True, pasos[0], list(camino)
                pasos[0] += 1
                print(f"Paso {pasos[0]}: ({f + 1},{c + 1}) no sirve como inicio")

    return False, pasos[0], []


def ejecutar():
    print("\n--- Sopa de letras ---")
    ruta_sopa = obtener_ruta_sopa()

    try:
        cuadricula = cargar_sopa(ruta_sopa)
    except Exception as e:
        print(f"Error al cargar '{ruta_sopa}': {e}")
        return

    print(f"Cuadrícula cargada desde {ruta_sopa.name} (10 x 10)")
    mostrar_cuadricula(cuadricula)

    while True:
        palabra = pedir_palabra()
        print(f'\nBusco "{palabra}" ({len(palabra)} letras).')
        encontrada, total_pasos, camino = buscar_palabra(cuadricula, palabra)

        if encontrada:
            print(f"\n¡Encontrada en {total_pasos} pasos!")
            dibujar_recorrido(cuadricula, palabra, camino)
        else:
            print(f'\n"{palabra}" no se puede formar en esta sopa.')

        while True:
            resp = input("\n¿Buscar otra palabra? (s/n): ").strip().lower()
            if resp in ("s", "si", "sí", "n", "no"):
                break
            print("Error: responda 's' o 'n'.")

        if resp in ("n", "no"):
            break


if __name__ == "__main__":
    ejecutar()