## write a program to count the number of vowels and consonants in a given string

string = input("Enter a string: ")
vowels = 0
consonants = 0  

for char in string:
    if char.isalpha():  # Check if the character is an alphabet
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)