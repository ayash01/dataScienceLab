import numpy as np

numbers = input("Enter a list of numbers separated by spaces: ").split()

array = np.array([int(i) for i in numbers])

print("Mean:", np.mean(array))
print("Median:", np.median(array))
print("Standard Deviation:", np.std(array))