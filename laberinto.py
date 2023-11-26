# Dimensiones del laberinto
filas = 5
columnas = 5

# Tupla con coordenadas de las casillas donde hay muro
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Iniciar el laberinto con espacios en blanco
laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]

# Marcar las casillas correspondientes como muros (X)
for coordenada in muro:
    fila, columna = coordenada
    laberinto[fila][columna] = 'X'

# Imprimir el laberinto
for fila in laberinto:
    print(' '.join(fila))