# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

student_name = "ThankGod"
student_age = 22
gpa_score = 4.65
is_active = True

print("Name:", student_name, "| Type:", type(student_name))
print("Age:", student_age, "| Type:", type(student_age))
print("GPA:", gpa_score, "| Type:", type(gpa_score))
print("Active Status:", is_active, "| Type:", type(is_active))


# Exercise 2: Two-Number Calculator

print("--- Exercise 2: Two-Number Calculator ---")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0:
  print("Quotient:", num1 / num2)
  print("Remainder:", num1 % num2)
else:
  print("Quotient: Undefined (division by zero)")
  print("Remainder: Undefined (division by zero)")
print()

# ── Exercise 3: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_output = (celsius_input * 9 / 5) + 32
print(f"{celsius_input}°C is equal to {fahrenheit_output:.2f}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_output = (fahrenheit_input - 32) * 5 / 9
print(f"{fahrenheit_input}°F is equal to {celsius_output:.2f}°C")


# Exercise 4: Robot Sensor Monitor

print("--- Exercise 4: Robot Sensor Monitor ---")
robot_name = input("Enter Robot Name: ")
robot_id = int(input("Enter Robot ID (integer): "))
sensor_name = input("Enter Sensor Name: ")
sensor_reading = float(input("Enter Current Sensor Reading (float): "))
operating_limit = float(input("Enter Operating Limit (float): "))

difference = operating_limit - sensor_reading

print("\n========== ROBOT SENSOR REPORT ==========")
print(f"Robot Name     : {robot_name}")
print(f"Robot ID       : {robot_id}")
print(f"Sensor Name    : {sensor_name}")
print(f"Sensor Reading : {sensor_reading}")
print(f"Operating Limit: {operating_limit}")
print(f"Difference     : {difference:.2f}")
print("=========================================")



