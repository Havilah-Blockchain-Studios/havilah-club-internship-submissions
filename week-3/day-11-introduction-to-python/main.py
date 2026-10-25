# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: your code here
# Exercise 1

name = "Kennedy"
age = 20
height = 1.75
is_student = True

print("Name:", name)
print("Type:", type(name))

print("Age:", age)
print("Type:", type(age))

print("Height:", height)
print("Type:", type(height))

print("Student:", is_student)
print("Type:", type(is_student))

# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO: 
# Exercise 2

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in Celsius:", celsius)

# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# TODO: your code here
# Exercise 3

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2026
age = current_year - birth_year
years_to_30 = 30 - age

print("Name:", name)
print("Your current age:", age)
print("You will turn 30 in", years_to_30, "years")
