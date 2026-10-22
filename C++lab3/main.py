import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# rowInNeed = a.argmin() // a.shape[1]
# colInNeed = a.argmax() % a.shape[1]

rowInNeed = np.unravel_index(a.argmin(), a.shape)[0]
colInNeed = np.unravel_index(a.argmax(), a.shape)[1]

print(a)
print()
print(a[rowInNeed , :] @ a[:, colInNeed])