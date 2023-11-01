class MatrizVacia:
    def __init__(self):
        self.matriz = [[0 for _ in range(5)] for _ in range(5)]

    def ubicar_numero(self, fila, columna, numero):
        self.matriz[fila][columna] = numero

    def generar_secuencias(self,fila,columna):
        numero = 0
        for i in range(5):
            for j in range(5):
                if self.matriz[i][j] != 0 and (i==fila or j==columna):
                    numero = self.matriz[i][j]

        for i in range(5):
            for j in range(5):
                if self.matriz[i][j] == 0 and (i==fila or j==columna):
                    self.matriz[i][j] = numero + abs(i - fila) + abs(j - columna)

    

# Ejemplo de uso
if __name__ == "__main__":
    matriz_vacia = MatrizVacia()

