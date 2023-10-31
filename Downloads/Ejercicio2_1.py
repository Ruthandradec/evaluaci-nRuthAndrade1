class MatrizVacia:
    def __init__(self):
        self.matriz = [[0 for _ in range(5)] for _ in range(5)]

    def ubicar_numero(self, fila, columna, numero):
        self.matriz[fila][columna] = numero


if __name__ == "__main__":
    matriz_vacia = MatrizVacia()