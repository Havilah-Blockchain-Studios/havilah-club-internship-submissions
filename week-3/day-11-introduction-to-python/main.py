# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: 
name = "Ben" #string
age = 30 #integer
height = 1.78 #float
is_engineer = True #Boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Engineer?:", is_engineer)


# ── Exercise 2: Calculator ────────────────────────────────────────
# Create a program that asks the user to enter two numbers. Convert the inputs to numbers and display the sum, difference, product, quotient, and remainder. 
#Use clear labels for each result.

# TODO:
# Ask the user for two numbers

number1 = float(input("\nEnter the first number: "))
number2 = float(input("Enter the second number: "))

# Perform calculations

sum_result = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 / number2
remainder = number1 % number2

# Display results

print("\n Calculator Results ")
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", remainder)


# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Temperature Converter: Create a program that asks the user to enter a temperature in Celsius and converts it to Fahrenheit. 
# Then ask for a temperature in Fahrenheit and convert it to Kelvin. The program should accept decimal values.

# TODO:
# Celsius to Fahrenheit

celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Fahrenheit to Kelvin

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
kelvin = (fahrenheit_input - 32) * 5 / 9 + 273.15
print("Temperature in Kelvin:", kelvin)

#——— Exercise 4: 
# Robot Sensor Monitor: Build a simple Python program that simulates the collection of data from a robot sensor. 
# Your program should ask the user for the Robot Name, Robot ID, Sensor Name, Sensor Reading, and Operating Limit. Convert the sensor reading and operating limit to appropriate numerical types. 
#Calculate the difference between the operating limit and the current sensor reading. Finally, display a clearly formatted reporkt.

# Collect robot information

robot_name = input("\nEnter Robot Name: ")

robot_id = input("Enter Robot ID: ")

sensor_name = input("Enter Sensor Name: ")

# Convert sensor values to numbers

sensor_reading = float(input("Enter Sensor Reading: "))

operating_limit = float(input("Enter Operating Limit: "))

# Calculate difference

difference = operating_limit - sensor_reading

# Display report

print("\n ROBOT SENSOR REPORT ")
print("Robot Name:", robot_name)
print("Robot ID:", robot_id)
print("Sensor Name:", sensor_name)
print("Sensor Reading:", sensor_reading)
print("Operating Limit:", operating_limit)
print("Difference:", difference)
