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

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(fila)

# Ejemplo de uso
if __name__ == "__main__":
    matriz_vacia = MatrizVacia()

    numero = int(input("Ingrese el número a ubicar en la matriz: "))
    fila = int(input("Ingrese la fila para ubicar el número (0-4): "))
    columna = int(input("Ingrese la columna para ubicar el número (0-4): "))

    if 0 <= fila < 5 and 0 <= columna < 5:
        matriz_vacia.ubicar_numero(fila, columna, numero)
        matriz_vacia.generar_secuencias(fila,columna)

        print("Matriz generada con secuencias:")
        matriz_vacia.mostrar_matriz()
    else:
        print("La ubicación ingresada está fuera del rango de la matriz.")
