# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: your code here
Name = "Chigozie"
Age = 20
Is_an_engineer = True
Rating = 4.9

print(Name)
print(Age)
print(Is_an_engineer)
print(Rating)

print(type(Name))
print(type(Age))
print(type(Is_an_engineer))
print(type(Rating))

# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO: your code here
# celsius to fahrenheit
Temp = float(input("Enter temperature in celsius: "))
conversion = (Temp * 9/5) + 32
print(Temp, "degree celsuis converted to", conversion,"degree fahrenheit")

# fahrenheit to celsuis
Temp = float(input("Enter temperature in fahrenheit: "))
conversion = (Temp - 32) * 5/9
print(Temp, "degree fahrenheit converted to", conversion,"degree celsius")


# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# TODO: your code here
User_Name = input("Enter your name> ")
Birth_year = int(input("Enter your birth year> "))
future_year = Birth_year + 30
print("You will be 30 years old by", future_year)