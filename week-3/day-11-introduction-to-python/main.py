# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

#string
name = "Miracle"
#integer
age = 20
#float
height = 1.78
#boolean
student = True

print("name")
print (age)
print(height)
print(student)
#str



# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).


celcius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celcius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celcius = (fahrenheit - 32) * 5/9
print(f"Temperature in Celsius: {celcius}")




# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.


name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2023
age = current_year - birth_year
year_turn_30 = birth_year + 30


print(f"Hello, {name}!")
print(f"You are currently {age} years old.")
print(f"You will turn 30 in the year {year_turn_30}.")
