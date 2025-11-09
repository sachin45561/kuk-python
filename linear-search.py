# Linear Search in Python

# List of numbers
numbers = [10, 25, 30, 45, 60, 75, 90]

# Number to search
target = int(input("Enter the number to search: "))

# Flag to check if found
found = False

# Traverse the list
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Number found at index {i}")
        found = True
        break

if found == False:
    print("Number not found in the list.")
