import numpy as np

low = float(input("Enter lower bound of uniform distribution: "))
high = float(input("Enter upper bound of uniform distribution: "))

rows = int(input("Enter number of rows of output array: "))
cols = int(input("Enter number of columns of output array: "))

random = np.random.uniform(low, high, (rows, cols))

print(random)

