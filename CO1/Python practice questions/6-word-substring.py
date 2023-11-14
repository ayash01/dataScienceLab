count = int(input("Enter number of words in list: "))

print("Enter", count, "words: ")
list = []
for i in range(count):
    list.append(input())

name = input("Enter a substring: ")

print("Entered list: ", list)

out = []
namecount = 0
occurence = []

for word in list:
    if name in word:
        namecount += 1
        occurence.append(i)
    else:
        occurence.append(0)

out.append(namecount)
out.append(occurence)

print(tuple(out))
