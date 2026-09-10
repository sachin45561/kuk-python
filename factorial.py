## Write a Python program to find the factorial of a number provided by the user.

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    
    for i in range(1, num + 1):
        factorial = factorial * i

    print("Factorial =", factorial)

## using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print("Factorial =", result)