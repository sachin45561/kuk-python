def check_triangle_type(a, b, c):
    # Step 1: Validate if the sides can form a triangle
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not a valid triangle"
    
    # Step 2: Determine the type of triangle based on side lengths
    if a == b == c:
        return "Equilateral Triangle (All sides are equal)"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle (Two sides are equal)"
    else:
        return "Scalene Triangle (All sides are different)"

# --- Example Usage ---
# Example 1: Valid Equilateral
print(f"Sides 5, 5, 5: {check_triangle_type(5, 5, 5)}")

# Example 2: Valid Isosceles
print(f"Sides 5, 5, 3: {check_triangle_type(5, 5, 3)}")

# Example 3: Valid Scalene
print(f"Sides 3, 4, 5: {check_triangle_type(3, 4, 5)}")

# Example 4: Invalid Triangle
print(f"Sides 1, 2, 5: {check_triangle_type(1, 2, 5)}")
