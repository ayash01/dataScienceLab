import numpy as np

array = np.array([[55, 25, 15, 12], 
                  [30, 44, 21, 98], 
                  [11, 45, 77, 23],
                  [90, 56, 31, 87]])

print("Determinant of given matrix: ", np.linalg.det(array))
print("Inverse of given matrix: ", np.linalg.inv(array))