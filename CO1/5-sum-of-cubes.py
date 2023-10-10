def sumOfCubes(number):
    if number <= 0:
        return 0
    else:
        sum = 0
        for i in range(1, num + 1):
            sum += (i * i * i)
        return sum

num = int(input("Enter a positive number: "))

print("The sum of cubes is", sumOfCubes(num))