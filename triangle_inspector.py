# Project: Geometry Triangle Inspector
# Description: Calculates properties of a triangle based on 3 coordinates (x,y).
# Concepts: Functions, Math Library, Geometry Logic.

import math

def read_points():
    """Reads coordinates from user input string 'x1,y1,x2,y2,x3,y3'."""
    try:
        points = input("Enter points (format: x1,y1,x2,y2,x3,y3): ")
        L = [float(t.strip()) for t in points.split(",")]
        if len(L) != 6:
            raise ValueError
        return (L[0], L[1]), (L[2], L[3]), (L[4], L[5])
    except:
        print("Invalid format. Please try again.")
        return None, None, None

def distance(p, q):
    """Calculates Euclidean distance between two points."""
    return math.hypot(p[0] - q[0], p[1] - q[1])

def is_valid_triangle(a, b, c):
    """Checks if sides can form a real triangle."""
    return (a + b > c) and (b + c > a) and (c + a > b)

def perimeter(a, b, c):
    return a + b + c

def area(a, b, c):
    """Calculates area using Heron's formula."""
    s = (a + b + c) / 2.0
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def type_by_sides(a, b, c):
    if math.isclose(a, b) and math.isclose(b, c):
        return "Equilateral"
    if math.isclose(a, b) or math.isclose(b, c) or math.isclose(c, a):
        return "Isosceles"
    return "Scalene"

def type_by_angles(a, b, c):
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]
    left = round(a*a + b*b, 4)
    right = round(c*c, 4)
    
    if left == right:
        return "Right-angled"
    return "Acute-angled" if left > right else "Obtuse-angled"

# --- Main Program ---
print("=== Triangle Inspector Tool ===")
A, B, C = read_points()

if A and B and C:
    # Calculate lengths of sides
    ab = distance(A, B)
    bc = distance(B, C)
    ca = distance(C, A)
    
    print(f"\nSide lengths: AB={ab:.4f}, BC={bc:.4f}, CA={ca:.4f}")
    
    if not is_valid_triangle(ab, bc, ca):
        print("Error: These points do not form a valid triangle.")
    else:
        print("\n--- Results ---")
        print(f"Perimeter: {perimeter(ab, bc, ca):.4f}")
        print(f"Area:      {area(ab, bc, ca):.4f}")
        print(f"Type (Sides):  {type_by_sides(ab, bc, ca)}")
        print(f"Type (Angles): {type_by_angles(ab, bc, ca)}")
