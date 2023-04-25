import numpy as np

I = [
    [1, 4, 6],
    [3, 2, 1],
    [6, 8, 2],
]

I = np.asarray(I)

print("Median", np.median(I))
print("Mittelwert", np.average(I))
