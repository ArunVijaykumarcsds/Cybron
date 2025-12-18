"""
Python Programming Internship - Cybrom Technology Pvt. Ltd.
Program: Multiplication Tables and Control Flow Demonstrations
Author: Arun VK
Topic: Loops, Conditional Statements, and Multiplication Tables
"""

# =====================================================
# Program 1: Basic Multiplication Table
# =====================================================
print("=" * 50)
print("Program 1: Basic Multiplication Table")
print("=" * 50)

a = int(input("Enter any number: "))
for i in range(1, 11):
    print(a, "x", i, "=", i * a)

print()

# =====================================================
# Program 2: Conditional Multiplication Tables
# Prints table if number is divisible by 2
# =====================================================
print("=" * 50)
print("Program 2: Conditional Multiplication Table (Even Check)")
print("=" * 50)

b = int(input("Enter any number: "))
if b % 2 == 0:
    for i in range(1, 11):
        print(b, "x", i, "=", b * i)
else:
    print(f"{b} is not divisible by 2. Table not printed.")

print()

# =====================================================
# Program 3: Nested Conditional with Multiplication
# Checks if number is divisible by 2, then checks for other conditions
# =====================================================
print("=" * 50)
print("Program 3: Advanced Conditional Multiplication")
print("=" * 50)

c = int(input("Enter any number: "))
if c % 2 == 0:
    print(f"{c} is divisible by 2")
    for i in range(1, 11):
        print(c, "x", i, "=", c * i)
elif c % 2 != 0:
    print(f"{c} is NOT divisible by 2")
    for j in range(1, 11):
        if j % 2 != 0:
            print(j * j)
else:
    print("Invalid input")

print()

# =====================================================
# Program 4: Multiple Number Multiplication Tables
# =====================================================
print("=" * 50)
print("Program 4: Multiple Multiplication Tables")
print("=" * 50)

# First number table
num1 = int(input("Enter first number: "))
print(f"\nMultiplication table of {num1}:")
for i in range(1, 11):
    print(f"{num1} x {i} = {num1 * i}")

# Second number table
num2 = int(input("\nEnter second number: "))
print(f"\nMultiplication table of {num2}:")
for i in range(1, 11):
    print(f"{num2} x {i} = {num2 * i}")

# Third number table
num3 = int(input("\nEnter third number: "))
print(f"\nMultiplication table of {num3}:")
for i in range(1, 11):
    print(f"{num3} x {i} = {num3 * i}")

print()

# =====================================================
# Program 5: Squares of Numbers (Conditional)
# =====================================================
print("=" * 50)
print("Program 5: Squares of Odd Numbers")
print("=" * 50)

limit = int(input("Enter limit: "))
print(f"\nSquares of odd numbers from 1 to {limit}:")
for i in range(1, limit + 1):
    if i % 2 != 0:
        print(f"{i}^2 = {i * i}")

print()

# =====================================================
# Program 6: Even/Odd Number Checker with Tables
# =====================================================
print("=" * 50)
print("Program 6: Even/Odd Checker with Multiplication")
print("=" * 50)

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is EVEN")
    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
else:
    print(f"{number} is ODD")
    print("Squares of numbers from 1 to 10:")
    for j in range(1, 11):
        print(f"{j}^2 = {j * j}")

print()

# =====================================================
# Program 7: Range-based Multiplication Practice
# =====================================================
print("=" * 50)
print("Program 7: Custom Range Multiplication")
print("=" * 50)

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
multiplier = int(input("Enter multiplier: "))

print(f"\nMultiplying numbers from {start} to {end} by {multiplier}:")
for i in range(start, end + 1):
    print(f"{i} x {multiplier} = {i * multiplier}")

print()
print("=" * 50)
print("All Programs Completed Successfully!")
print("=" * 50)