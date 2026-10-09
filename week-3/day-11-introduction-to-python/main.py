# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: your code here

# Creating variables for an engineer
professional_title = "Robotics Engineer"  # String
years_experience = 7                      # Integer
hourly_rate = 52.50                       # Float
is_certified = True                       # Boolean

print("Title:", professional_title, "|type:", type(professional_title))  # Descriptive Label

print("Years_experience:", "|type:", type(years_experience) )  # Descriptive Label

print("Hourly_rate:", "|type:", type(hourly_rate))        # Descriptive Label

print("Certified:", "|type:", type(is_certified))       # Descriptive Label


# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO: your code here

# This program converts celsius to fahrenheit
# ask for user inputs
c = float(input("Enter value of Temperature in Celsius: "))

# Define Celsius to Fahrenheit formula

f = c * (9.0 / 5.0) + 32.0

# Print Celsius Value

print("Temperature in Celsius: ",c)

# print fahrenheit value
f2 = float(input("Enter value of Temperature in fahrenheit: "))
c2 = (f2 - 32) * 5.0 /9.0
print("Temperature in Fahrenheit:", f2)
print("Temperature in celsius:", c2)

# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# TODO: your code here


# Inputs

name = input("What is your name: ")
birth_year = int(input("Enter your birth_year: "))
current_year = int(input("Enter your current year: "))


# Process

age = current_year - birth_year
year_turning_30 = birth_year + 30


# Output

print("Hi",name,"you are",age,"years old",)
print("you will be 30 years old in",year_turning_30)
