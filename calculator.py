def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation"
# Example usage:
result = calculator(10, 5, 'add') # result would be 15    
print(result)    