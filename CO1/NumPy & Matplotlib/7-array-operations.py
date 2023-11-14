import numpy as np

numbers = input("Enter a list of numbers separated by spaces: ").split()
arr1 = np.array([int(i) for i in numbers])

numbers = input("Enter another list of numbers separated by spaces: ").split()
arr2 = np.array([int(i) for i in numbers])

print("Addition:", np.add(arr1, arr2))
print("Subtraction:", np.subtract(arr1, arr2))
print("Multiplication:", np.multiply(arr1, arr2))
print("Division:", np.divide(arr1, arr2))





