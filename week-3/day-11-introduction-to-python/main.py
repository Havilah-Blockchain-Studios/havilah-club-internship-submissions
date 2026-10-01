# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# String
name = "Emmanuel"

# Integer
age = 21

# Float
height = 1.75

# Boolean
is_student = True

# Print values with descriptive labels
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Print the data types
print("Name type:", type(name))
print("Age type:", type(age))
print("Height type:", type(height))
print("Is Student type:", type(is_student))


# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# Ask for temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# Ask for temperature in Fahrenheit
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius_result = (fahrenheit_input - 32) * 5 / 9

print("Temperature in Celsius:", celsius_result)


# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# Ask for the user's name and birth year
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

# Get the current year
current_year = 2026

# Calculate current age
age = current_year - birth_year

# Calculate the year they will turn 50
year_turn_50 = birth_year + 50

# Display the results
print("Name:", name)
print("Current age:", age)
print("You will turn 50 in:", year_turn_50)
