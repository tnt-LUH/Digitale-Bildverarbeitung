import numpy as np

M = np.zeros((10, 10))
for i in range(10):
    for j in range(10):
        M[i, j] = 10 * i + j

print("(1) M=", M)

v = np.ones((1, 10)) * 20
print("(2) v=", v)

vr = v - M[1, :]
print("(3) vr:", vr)

res = np.matmul(M, np.transpose(vr, axes=(1, 0)))
print("(4) res:", res)

res = res / 100
res = np.round(res)  # np.floor() np.ceil()
print("(5) res:", res)

maximum = np.max(res)
print("(6) maximum:", maximum)
