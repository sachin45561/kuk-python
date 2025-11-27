import math

# --- Constants ---
print(f"Value of Pi (π): {math.pi}")
print(f"Value of e: {math.e}")

# --- Rounding Functions ---
x = 7.6
print(f"\nOriginal value: {x}")
print(f"Ceil (rounds up): {math.ceil(x)}")
print(f"Floor (rounds down): {math.floor(x)}")

# --- Power and Absolute Value ---
print(f"\n2 to the power of 4: {math.pow(2, 4)}")
print(f"Absolute value of -5.5: {math.fabs(-5.5)}")

# --- Trigonometric Functions (x in radians) ---
# Use math.radians() to convert degrees to radians if needed
angle_rad = math.pi / 4  # 45 degrees
print(f"\nAngle in radians (π/4): {angle_rad}")
print(f"Sine: {math.sin(angle_rad)}")
print(f"Cosine: {math.cos(angle_rad)}")
print(f"Tangent: {math.tan(angle_rad)}")