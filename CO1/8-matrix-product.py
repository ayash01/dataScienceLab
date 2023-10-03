import numpy as np

def inputMatrix(number):
    print(f"Enter details for Matrix {number}:")
    rows = int(input("Enter number of rows of matrix: "))
    cols = int(input("Enter number of columns of matrix: "))

    print("Enter elements of matrix in a single line separated by a space: ")
    elements = list(map(int, input().split()))

    mat = np.array(elements).reshape(rows, cols)
    print(f"Matrix {number}: ", mat)
    return mat

matA = inputMatrix(1)
matB = inputMatrix(2)

print("Product of matrices:", np.multiply(matA, matB))

