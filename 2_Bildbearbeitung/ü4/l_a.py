import numpy as np


""" Erstellen des Ursprünglichen Filterkerns"""
f_a = np.expand_dims(np.asarray([1, 4, 1]), 0)
f_b = np.expand_dims(np.asarray([-1, 0, 1]), 1)
f_orig = np.matmul(f_b, f_a)
print("TEIL 1")
print(f_a)
print(f_b)
print(f_orig)

""" Separieren des Filterkerns

Wir können das Problem als

f_a * f_b = f_C

mit

f_a = [a, b, c]^T
f_b = [d, e, f]

f_C = [
  [ ad, ae, af ],
  [ bd, be, bf ],
  [ cd, ce, cf ],
]

modellieren. Wenn wir a=1 setzten, ergibt sich d=-2 e=-3 f=-2 (erste Zeile der Matrix) sodass sich ein linear 
unabhängiges Gleichungssystem 
f_C = [
  [ -2a, -3a, -2a ],
  [ -2b, -3b, -2b ],
  [ -2c, -3c, -2c ],
] =
[
  [-2, -3, -2],
  [0, 0, 0],
  [2, 3, 2],
]

=> -2a=-2, -2b=0, -2c=2

=> A * x = B 
A = [
  [-2, 0,  0],
  [ 0, -2,  0],
  [ 0, 0, -2],
]
x = [a, b, c]^T
B = [-2, 0, 2]^T


erstellen lässt. Dieses lässt sich leicht "von Hand" oder mit Numpy lösen.
=>
f_a = [1, 0, -1]^T
f_b = [-2, -3, -2]
Hinweis: Es gibt unendlich viele Lösungen (wenn separierbar)!
"""
f_C = np.asarray(
    [
        [-2, -3, -2],
        [0, 0, 0],
        [2, 3, 2],
    ]
)

A = np.array([
  [-2, 0, 0],
  [ 0,-2, 0],
  [ 0, 0,-2],
])
B = np.array([-2, 0, 2])
x = np.linalg.solve(A, B)

f_a = np.expand_dims(x, axis=1)
f_b = np.expand_dims(np.asarray([-2, -3, -2]), axis=0)
f_C_new = np.matmul(f_a, f_b)
print("TEIL 2")
print(f_C)
print(f_C_new)
