#Ingeniería eléctrica

import numpy as np
G = np.array([[0.75, -0.5],
              [-0.5, 0.8333333333333333]])
I = np.array([2.0, -1.0])
V = np.linalg.solve(G, I)
print("V (voltios) =", V)

#Ingeniería civil y mecánica
import numpy as np
E = 210e9  # Pa
A = 0.01   # m2
L = 1.0    # m
k = E*A/L
K = np.array([[2*k, -k],
              [-k,  k]])
F = np.array([0.0, 1000.0])
u = np.linalg.solve(K, F)
print("Desplazamientos (m) en nodos [2,3] =", u)

#Ingeniería informática
import numpy as np
theta = np.pi/4
Rz = np.array([[np.cos(theta), -np.sin(theta), 0],
               [np.sin(theta),  np.cos(theta), 0],
               [0, 0, 1]])
S = np.diag([2.0, 0.5, 1.0])
t = np.array([1.0, -2.0, 0.5])
M = S.dot(Rz)
T = np.eye(4)
T[:3,:3] = M
T[:3,3] = t
p = np.array([1.0, 1.0, 1.0, 1.0])
p_trans = T.dot(p)
print("Punto transformado (x,y,z,1):", p_trans)

#Ingeniería industrial y economía
import numpy as np
A = np.array([[0.2, 0.1, 0.0],
              [0.3, 0.1, 0.2],
              [0.1, 0.0, 0.1]])
d = np.array([50.0, 80.0, 30.0])
I = np.eye(3)
L = np.linalg.inv(I - A)
x = L.dot(d)
print("Matriz de Leontief L = (I-A)^-1:\n", L)
print("Producción total requerida x:\n", x)

