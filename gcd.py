# Function to compute GCD using the Euclidean algorithm
def gcd(a, b):
    if a == 0 and b == 0:
        return None  # GCD undefined
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculating and printing the GCD
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))