# Ejercicio 1: suma de matrices 4x4
import numpy as np
A = np.array([[1,2,3,4],[5,6,7,8],[9,1,2,3],[4,5,6,7]])
B = np.array([[4,3,2,1],[8,7,6,5],[3,2,1,9],[7,6,5,4]])
# np.add realiza la suma entrada a entrada
S = np.add(A, B)
print("Resultado A+B:\n", S)

#Ejercicio 2
import numpy as np
A = np.array([[6,1,4,4,8],[4,6,3,5,8],[7,9,9,2,7],[8,8,9,2,6],[9,5,4,1,4]])
B = np.array([[6,1,3,4,9],[2,4,4,4,8],[1,2,1,5,8],[4,3,8,3,1],[1,5,6,6,7]])
S = A + B  # alternativa a np.add
print(S)

#Ejercicio 3
import numpy as np
A = np.array([[3,1,5,2],[6,4,3,1],[8,7,2,0],[5,2,9,1]])
B = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
print(A + B)


#Ejercicio 4
import numpy as np
A = np.array([[10,8,6,4],[9,7,5,3],[8,6,4,2],[7,5,3,1]])
B = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
print(A - B)


#Ejercicio 5
import numpy as np
A=np.array([[15,18,19,15,10],[10,11,17,16,19],[12,14,15,12,14],[12,14,17,17,19],[11,17,10,16,19]])
B = np.array([[8,7,2,1,2],[9,9,4,9,8],[4,7,6,2,4],[5,9,2,5,1],[4,3,1,5,3]])
print(A - B)


#Ejercicio 6
import numpy as np
A = np.array([[9,8,7,6],[5,4,3,2],[1,0,1,2],[3,4,5,6]])
B = np.array([[0,1,2,3],[4,3,2,1],[1,1,1,1],[6,5,4,3]])
print(A - B)


#Ejercicio 7
import numpy as np
A = np.array([[1,1,4,3],[4,1,3,2],[4,3,5,5],[5,4,5,3]])
B = np.array([[3,1,2,4],[1,1,1,4],[3,4,2,2],[3,1,5,5]])
# np.dot realiza producto matricial
P = A.dot(B)
print("A·B =\n", P)


#Ejercicio 8
import numpy as np
A = np.array([[2,1,0,3],[1,2,3,1],[0,1,4,2],[3,0,2,1]])
B = np.array([[1,0,2,1],[0,3,1,2],[4,1,0,3],[2,3,1,0]])
print(A.dot(B))


#Ejercicio 9
import numpy as np
A = np.array([[8,6,2,9,8],[9,3,8,8,8],[9,5,3,7,5],[4,1,8,6,6],[7,7,9,3,6]])
B = np.array([[4,7,7,1,9],[5,8,1,1,8],[2,6,8,1,2],[5,7,3,2,3],[8,1,6,1,1]])
print(A.dot(B))