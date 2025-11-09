# Matrix Multiplication using nested loops
#result[i][j]=k=0∑n−1​(mat1[i][k]∗mat2[k][j])

# Define two matrices
mat1 = [
    [1, 2, 3],
    [4, 5, 6]
]

mat2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Create an empty result matrix with zeros
result = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]

# Perform matrix multiplication
for i in range(len(mat1)):            # Rows of mat1
    for j in range(len(mat2[0])):     # Columns of mat2
        for k in range(len(mat2)):    # Common dimension
            result[i][j] += mat1[i][k] * mat2[k][j]

# Display the result
print("Resultant Matrix:")
for row in result:
    print(row)
