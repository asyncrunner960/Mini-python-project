from math import sqrt

# Quadratic Equation Solver
# Finds the real roots of a quadratic equation: a * x^2 + b * x + c = 0

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Handle the case where a = 0 (not a quadratic equation)
if a == 0:
    print("Error: coefficient 'a' cannot be zero for a quadratic equation.")
else:
    d = (b ** 2) - 4 * (a * c)  # Discriminant
    root1 = -b / (2 * a)

    if d == 0:
        # One repeated real root
        print(root1)
    elif d > 0:
        # Two distinct real roots
        root2 = (-b - sqrt(d)) / (2 * a)
        root3 = (-b + sqrt(d)) / (2 * a)
        print(*sorted([root2, root3]), sep="\n")
    else:
        # No real roots (d < 0)
        print("No real roots")
