import math

# Read the shape
shape = input().strip()

# Read measurements and calculate area
if shape == 'rectangle':
    n = float(input())
    m = float(input())
    area = m * n

elif shape == 'triangle':
    n = float(input())
    m = float(input())
    area = 1 / 2 * m * n

elif shape == 'circle':
    n = float(input())
    area = math.pi * n * n
# Print the area
print(f"Area: {area}")
