# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: your code here
student_name = "victor"
student_age = 20
student_height = 5.9
is_student = True

print(f"Student Name: {student_name}")
print(f"Student Age: {student_age}")
print(f"Student Height: {student_height}")
print(f"Is Student: {is_student}")

# ── Exercise 2:  ────────────────────────────────────────
#Create a program that asks the user to enter two numbers.
# Convert the inputs to numbers and display the sum, difference, product, quotient, and remainder.
#Use clear labels for each result.


# TODO: your code here
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined"
remainder = num1 % num2 if num2 != 0 else "undefined"

print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")

# ── Exercise 3: Temperature Converter ────────────────────────────────────────────────
# Create a program that asks the user to enter a temperature in Celsius and converts it to Fahrenheit.
# Then ask for a temperature in Fahrenheit and convert it to Kelvin. The program should accept decimal values.

# TODO: your code here
celcius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celcius * 9/5) + 32
print(f"{celcius}°C is equal to {fahrenheit}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
kelvin = (fahrenheit_input - 32) * 5/9 + 273.15
print(f"{fahrenheit_input}°F is equal to {kelvin}K")


# Robot Sensor Monitor: Build a simple Python program that simulates the collection of data from a robot sensor.
#Your program should ask the user for the Robot Name, Robot ID, Sensor Name, Sensor Reading, and Operating Limit.
#Convert the sensor reading and operating limit to appropriate numerical types.
#Calculate the difference between the operating limit and the current sensor reading. Finally, display a clearly formatted report.


# TODO: your code here
robot_name = input("Enter Robot Name: ")
robot_id = input("Enter Robot ID: ")        
sensor_name = input("Enter Sensor Name: ")
sensor_reading = float(input("Enter Sensor Reading: "))
operating_limit = float(input("Enter Operating Limit: "))

difference = operating_limit - sensor_reading

print(f"Robot Name: {robot_name}")
print(f"Robot ID: {robot_id}")
print(f"Sensor Name: {sensor_name}")
print(f"Sensor Reading: {sensor_reading}")
print(f"Operating Limit: {operating_limit}")
print(f"Difference: {difference}")