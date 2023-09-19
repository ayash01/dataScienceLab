import math

def sin(x, n):
    sinx = 0
    for i in range(1, n):
        sinx = (math.pow(x, i) / math.factorial(i)) - sinx

    return sinx

degree = float(input("Enter degree: "))

terms = int(input("Enter number of terms: "))

print("sin(x) = ", sin(degree, terms))