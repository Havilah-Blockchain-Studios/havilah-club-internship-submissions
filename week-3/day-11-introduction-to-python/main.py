# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

name = "Samuel"
age = 20
gpa = 4.75
is_enrolled = True

print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("GPA:", gpa, "| Type:", type(gpa))
print("Enrolled:", is_enrolled, "| Type:", type(is_enrolled))


# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_converted = (fahrenheit_input - 32) * 5/9
print(f"{fahrenheit_input}°F is {celsius_converted}°C")


# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

user_name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2026
current_age = current_year - birth_year
turning_year = current_year + (30 - current_age) if current_age < 30 else current_year

print(f"Hello {user_name}, you are {current_age} years old.")
print(f"You will turn 30 in the year {current_year + (30 - current_age)}.")
