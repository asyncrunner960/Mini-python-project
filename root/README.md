README.md
# Quadratic Equation Solver

A Python program to find the real roots of a quadratic equation `ax² + bx + c = 0`.
Uses the discriminant method to determine the number of roots.

## Features
- Calculates two distinct real roots when discriminant > 0
- Calculates one repeated real root when discriminant = 0
- Handles the case when `a = 0` with a clear error message
- Outputs roots sorted in ascending order
- Input validation prevents crashes on invalid data

## How to Run
1. Make sure you have Python 3 installed
2. Download `root.py`
3. Open terminal and run:
```
python root.py
```
4. Enter coefficients a, b, c when prompted

## Example
```
Enter coefficient a: 1
Enter coefficient b: -3
Enter coefficient c: 2
1.0
2.0
```
```
Enter coefficient a: 1
Enter coefficient b: 2
Enter coefficient c: 5
No real roots
``` 

## What I Learned
- Mathematical formulas and discriminant calculation
- Handling edge cases (a = 0, discriminant < 0)
- Sorting output with `sorted()`
- Type conversion and input validation
- Using the `sqrt()` function from the `math` module

## Tech
Python 3, `math` module
