num = int(input("Enter a positive number: "))

if num <= 0:
    print("Enter a positive number")
    SystemExit(0)
else:
    sum = 0
    for i in range(1, num+1):
        sum = sum + (i*i*i)
    print("The sum of cubes is", sum)