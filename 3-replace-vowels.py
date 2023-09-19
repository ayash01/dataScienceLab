def replaceVowels(string):
    for letter in string:
        if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
            string = string.replace(letter, '*')
    return string

text = input("Enter text: ")

print("Text with vowels replaced:", replaceVowels(text))