# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: name = "Alice"  # string
name = "Alice"
age = 30
height = 5.6
is_student = True

print(name)  # string
print(age)  # integer
print(height)  # float
print(is_student)  # boolean

# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO: celsius = float(input("Enter temperature in Celsius: "))

celsius = float(input("Enter temperature in Celsius"))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit", fahrenheit)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)

# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# TODO: name = input("Enter your name: ")
# TODO: birth_year = int(input("Enter your birth year: "))

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_age = 2026 - birth_year
year_turn_30 = birth_year + 30

print("your current age is:", current_age)
print("you will turn 30 in:", year_turn_30)

#Exercise 4: number converter

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Remainder:", a % b)

#Exercise 5: simmple robot monitor

Robot_name = input("Enter the robot's name: ")
Robot_ID = input("Enter the robot's ID: ")
Sensor_name = input("Enter the sensor's name: ")
Sensor_reading = float(input("Enter the sensor's reading: "))
Operating_limit = float(input("Enter the operating limit: "))

print("Robot Name:", Robot_name)
print("Robot ID:", Robot_ID)
print("Sensor Name:", Sensor_name)
print("Difference between operating limit and sensor reading:", Sensor_reading - Operating_limit)



print("All exercises completed successfully!")
