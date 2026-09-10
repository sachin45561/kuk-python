n = 5

for row in range(1, n + 1):
    stars = "*" * n
    print(stars)

# 1. Left-Aligned Triangle
# In row 1: print 1 star
# In row 2: print 2 stars
print("--- Left Triangle ---")
n = 5  # Height of the triangle
for row in range(1, n + 1):
    stars = "*" * row
    print(stars)

# 2. Right-Aligned Triangle
# In row 1: needs (n - 1) spaces, 1 star
# In row 2: needs (n - 2) spaces, 2 stars
print("\n--- Right Triangle ---")
n = 5  # Height of the triangle
for row in range(1, n + 1):
    spaces = " " * (n - row)
    stars = "*" * row
    print(spaces + stars)

# 3. Inverted Triangle
print("\n--- Inverted Triangle ---")
n = 5  # Height of the inverted triangle
for row in range(n, 0, -1):
        stars = "*" * row
        print(stars)

print("\n--- Inverted Right Triangle ---")
n = 5  # Height of the inverted triangle
for row in range(n, 0, -1):
    spaces = " " * (n - row)
    stars = "*" * row
    print(spaces + stars)

# 3. Pyramid
# Each row has an odd number of stars: (2 * row - 1) -> 1, 3, 5, 7...
print("\n--- Pyramid ---")
n = 5  # Height of the pyramid

for row in range(1, n + 1):
    spaces = " " * (n - row)
    stars = "*" * (2 * row - 1)
    print(spaces + stars)


# 4. Diamond (Pyramid + Inverted Pyramid)
print("\n--- Diamond ---")
n = 5  # Height of the diamond
# Top half
for row in range(1, n + 1):
    spaces = " " * (n - row)
    stars = "*" * (2 * row - 1)
    print(spaces + stars)

# Bottom half (counting backward from n-1 down to 1)
for row in range(n - 1, 0, -1):
    spaces = " " * (n - row)
    stars = "*" * (2 * row - 1)
    print(spaces + stars)


n = 5 # Height of the square
print("\n--- Square ---")
for row in range(1, n + 1):
    for col in range(1, n + 1):
        if row == 1 or row == n or col == 1 or col == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Move to the next line after each row