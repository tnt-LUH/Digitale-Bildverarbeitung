import numpy as np


""" Erstellen des Ursprünglichen Filterkerns"""
f_a = np.expand_dims(np.asarray([1, 4, 1]), 0)
f_b = np.expand_dims(np.asarray([-1, 0, 1]), 1)
f_orig = np.matmul(f_b, f_a)
print(f_a)
print(f_b)
print(f_orig)