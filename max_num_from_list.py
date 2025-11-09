#Write a program to find the maximum of a list of numbers

numbers = [10, 25, 8, 99, 54, 32]

# Assume the first number is the maximum
maximum = numbers[0]

# Compare each number with the current maximum
for num in numbers:
    if num > maximum:
        maximum = num

print("The maximum number in the list is:", maximum)
