# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: your code here
name = "JBryne"     #String
age = 23            #Integer
credits = 299.5     #Float
male = True         #Boolean
#Desriptive Labels
print((name), type(name))
print((age), type(age))
print((credits), type(credits))
print((male), type(male))

# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO: your code here
#Celcius to Farenheit
celcius_input = float(input("Enter Temperature in Celcius:" ))
fahrenheit_output = (celcius_input * 9 / 5) + 32
print("fahrenheit equivalent:", fahrenheit_output)

#Farenheit to Celcius
fahrenhiet_input = float(input("Enter Temperature in Farenheit:" ))
celcius_output = (fahrenhiet_input - 32) * 5 / 9
print("Celcius equivalent:", celcius_output)

# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# TODO: your code here
full_name = input("Enter your full name:" )
year_of_birth = int(input("Enter year of birth:" ))
current_year = 2026
current_age = current_year - year_of_birth
would_turn_30_in = year_of_birth + 30
print(f"Good day {full_name}, your current age is {current_age}, and you will be 30 by {would_turn_30_in}")