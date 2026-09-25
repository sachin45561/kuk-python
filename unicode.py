# This script prints all Unicode characters from code point 0 to 148999. 
# It uses the `chr()` function to convert each code point to its corresponding character. 
# If a `ValueError` occurs (which can happen for invalid code points), it will print an error message and break the loop.


for i in range(0, 149000,1):
    try:
        char = chr(i)
        print(char, end=' ')
    except ValueError:
        print(f"ValueError for code point: {i}")
        break

    