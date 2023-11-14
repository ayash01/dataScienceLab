import numpy as np

numbers = input("Enter a list of numbers separated by spaces: ").split()

array = np.array([int(i) for i in numbers])

print("Indices of elements equal to zero:", np.where(array == 0))