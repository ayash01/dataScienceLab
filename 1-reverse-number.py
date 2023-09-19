def sumOfDigits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum

def reverse(number):
    return str(number)[::-1]

num = int(input("Enter a number: "))

print("The sum of digits is", sumOfDigits(num))

print("The reversed number is", reverse(num))