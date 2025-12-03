import numpy as np

print(" SUMA DE MATRICES")

# Ejercicio 1 Suma 4x4
A1 = np.array([[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]])
B1 = np.array([[4,3,2,1],[8,7,6,5],[3,2,1,9],[7,6,5,4]])
print("Ejercicio 1:\n", A1 + B1, "\n")

# Ejercicio 2 Suma 5x5
A2 = np.random.randint(1,10,(5,5))
B2 = np.random.randint(1,10,(5,5))
print("Ejercicio 2:\n", A2 + B2, "\n")

# Ejercicio 3 Suma 4x4
A3 = np.array([[3,1,5,2],[6,4,3,1],[8,7,2,0],[5,2,9,1]])
B3 = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
print("Ejercicio 3:\n", A3 + B3, "\n")

print(" RESTA DE MATRICES")

# Ejercicio 4 Resta 4x4
C1 = np.array([[10,8,6,4],[9,7,5,3],[8,6,4,2],[7,5,3,1]])
D1 = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
print("Ejercicio 4:\n", C1 - D1, "\n")

# Ejercicio 5 Resta 5x5
C2 = np.random.randint(10,20,(5,5))
D2 = np.random.randint(1,10,(5,5))
print("Ejercicio 5:\n", C2 - D2, "\n")

# Ejercicio 6 Resta 4x4
C3 = np.array([[9,8,7,6],[5,4,3,2],[1,0,1,2],[3,4,5,6]])
D3 = np.array([[0,1,2,3],[4,3,2,1],[1,1,1,1],[6,5,4,3]])
print("Ejercicio 6:\n", C3 - D3, "\n")

print(" MULTIPLICACIÓN MATRICIAL")

# Ejercicio 7 Multiplicación 4x4
E1 = np.random.randint(1,6,(4,4))
F1 = np.random.randint(1,6,(4,4))
print("Ejercicio 7:\n", np.dot(E1, F1), "\n")

# Ejercicio 8 Multiplicación 4x4
E2 = np.array([[2,1,0,3],[1,2,3,1],[0,1,4,2],[3,0,2,1]])
F2 = np.array([[1,0,2,1],[0,3,1,2],[4,1,0,3],[2,3,1,0]])
print("Ejercicio 8:\n", np.dot(E2, F2), "\n")

# Ejercicio 9 Multiplicación 5x5
E3 = np.random.randint(1,10,(5,5))
F3 = np.random.randint(1,10,(5,5))
print("Ejercicio 9:\n", np.dot(E3, F3), "\n")

print(" PRODUCTO ESCALAR")
# Producto escalar: multiplicar un número por toda la matriz

# Ejercicio 10 Producto escalar 4x4
G1 = np.random.randint(1,10,(4,4))
print("Ejercicio 10:\n", 3 * G1, "\n")  # Escalar = 3

# Ejercicio 11 Producto escalar 5x5
G2 = np.random.randint(1,10,(5,5))
print("Ejercicio 11:\n", -2 * G2, "\n") # Escalar = -2

# Ejercicio 12 Producto escalar 4x4
G3 = np.random.randint(1,10,(4,4))
print("Ejercicio 12:\n", 5 * G3, "\n") # Escalar = 5


print(" DETERMINANTES")

# Ejercicio 13 Determinante 4x4
H1 = np.array([[1,2,3,4],[0,1,2,3],[5,4,3,2],[1,0,1,0]])
print("Ejercicio 13:", round(np.linalg.det(H1), 2), "\n")

# Ejercicio 14 Determinante 5x5
H2 = np.random.randint(1,6,(5,5))
print("Ejercicio 14:", round(np.linalg.det(H2), 2), "\n")

# Ejercicio 15 Determinante matriz singular → 0
H3 = np.array([[1,2,3,4],[2,4,6,8],[1,2,3,4],[0,1,0,1]])
print("Ejercicio 15:", round(np.linalg.det(H3), 2), "\n")
