"""
ÜBUNG 1

In dieser Übung soll der Umgang mit grundlegenden Matrix-Operationen mithilfe von numpy erlernt werden.

"""

import numpy as np

'''
a) Erstelle einen Zeilenvektor mit den Einträgen 1, 2, 3 
'''
A = [1, 2, 3]
A = np.asarray(A)
print("A", A)

'''
b) Erstelle einen Spaltenvektor mit den Einträgen 1, 2, 3 
'''
B = [[1], [2], [3]]
B = np.asarray(B)
print("B")
print(B)

B = [
        [1],
        [2],
        [3]
    ]
B = np.asarray(B)
print("B")
print(B)

'''
c) Erstelle eine 2x3 Matrix
'''
C = [
        [1, 2, 3],
        [4, 5, 6]
    ]
C = np.asarray(C)
print("C")
print(C)


'''
d) Erstelle eine 6x6 Matrix mit nur 0-Wert Einträgen
'''
D = np.zeros(shape=(6, 6))
print("D")
print(D)

'''
e) Erstelle eine 6x6 Matrix mit nur 1-Wert Einträgen
'''
E = np.ones(shape=(6, 6))
print("E")
print(E)

''' 
f) Erstelle eine 4x4 Einheitsmatrix 
'''
F = np.eye(4)
print("F")
print(F)

'''
g) Ändere den Wert aus f) aus der zweiten Zeile und dritten Spalte zu dem Wert 5 
'''
F[1, 2] = 5
print("G")
print(F)

'''
h) Ändere alle Werte aus f) aus der zweiten Zeile zu dem Wert 4.5 
'''
F[1] = 4.5
print("H")
print(F)

'''
i) Ändere die Werte aus f) aus der zweiten Zeile ab Spalte 3 zu dem Wert 3 
'''
F[1, 2:4] = 3
F[1, 2:] = 3
print("I")
print(F)

'''
j) Multipliziere, addiere, subtrahiere und dividiere die Matrizen a und b
'''
a = np.asarray([[1, 2], [3, 4]])
b = np.asarray([[5, 6], [7, 8]])

print("Elementweise Multiplikation")
print(
    a * b
)
print("Matrixoperation Multiplikation")
print(np.matmul(a, b))
print(a + b)
print(a - b)
