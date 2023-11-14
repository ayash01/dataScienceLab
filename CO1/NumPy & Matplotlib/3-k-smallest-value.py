import numpy as np

numbers = input("Enter a list of numbers separated by spaces: ").split()

array = np.array([int(num) for num in numbers])

k = int(input("Enter k: "))

kSmallest = np.partition(array, k)[:k]

print(f"The {k} smallest values are: {kSmallest}")