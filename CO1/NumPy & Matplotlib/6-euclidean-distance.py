import numpy as np

x1 = float(input("Enter x-coordinate of the 1st point: "))
y1 = float(input("Enter y-coordinate of the 1st point: "))

x2 = float(input("Enter x-coordinate of the 2nd point: "))
y2 = float(input("Enter y-coordinate of the 2nd point: "))

point1 = np.array([x1, y1])
point2 = np.array([x2, y2])

print("Euclidean distance:", np.linalg.norm(point2 - point1))

