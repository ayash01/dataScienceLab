def countCase(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper += 1
        else:
            lower += 1
    return upper, lower

text = input("Enter text: ")

upperCount, lowerCount = countCase(text)
print("Number of uppercase letters:", upperCount, "\nNumber of lowercase letters:", lowerCount)