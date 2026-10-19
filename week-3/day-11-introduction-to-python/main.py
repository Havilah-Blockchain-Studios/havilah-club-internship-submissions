# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Create variables representing ingormation about a student or engineer.
# TODO: your code here

# Vairiables for a Student
name = "Emmanuel"
age = 20
gpa = 4.7
is_student = True

print(name, type(name))
print(age, type(age))
print(gpa, type(gpa))
print(is_student, type(is_student))


# ── Exercise 2: Create a program that asks the user to enter two numbers.
# TODO: your code here

# Basic Arithmetic Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 % num2)


# ── Exercise 3: Temperature Converter:
# TODO: your code here

# Temperature Converter
celsius = float(input("Enter Celsius: "))
print("Fahrenheit:", (celsius * 9/5) + 32)

fahrenheit = float(input("Enter Fahrenheit: "))
print("Kelvin:", (fahrenheit - 32) * 5/9 + 273.15)


# ── Exercise 4: Robot Sensor Monitor:
# TODO: your code here

# Robot Sensor Monitor
robot_name = input("Robot Name: ")
robot_id = input("Robot ID: ")
sensor_name = input("Sensor Namee: ")
reading = float(input("Sensor Reading: "))
limit = float(input("Operating limit: "))

print("Robot Name  :", robot_name)
print("Robot ID    :", robot_id)
print("Sensor Name :", sensor_name)
print("Reading     :", reading)
print("Limit       :", limit)
print("Difference  :", limit - reading)