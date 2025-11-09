# take input from user
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

# calculate power
result = base ** exponent

print(base, "raised to the power of", exponent, "is", result)


# Using pow() function
result = pow(base, exponent)  
print("Using pow() function:", base, "raised to the power of", exponent, "is", result)