# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ============================================================
# EXERCISE 1: Student / Engineer Information
# ============================================================

print("===== ENGINEERING STUDENT INFORMATION VALIDATOR =====")

# Collects information from the user
name = input("Enter your fullname: ")
faculty = input("Enter your faculty: ")
department = input("Enter your department: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your current CGPA: "))

engineering_student_input = input(
    "Are you an engineering student? (yes/no): "
).strip().lower()

is_engineering_student = engineering_student_input == "yes"


# Display the information and data types
print("\n===== PROFILE =====")

print("Name:", name)
print("Data type:", type(name))

print("Faculty:", faculty)
print("Data type:", type(faculty))

print("Department:", department)
print("Data type:", type(department))

print("Age:", age)
print("Data type:", type(age))

print("CGPA:", cgpa)
print("Data type:", type(cgpa))

print("Engineering Student:", is_engineering_student)
print("Data type:", type(is_engineering_student))

# ============================================================
# EXERCISE 2: Basic Calculator
# ============================================================

print("\n===== BASIC CALCULATOR =====")

# Get two numbers from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Perform calculations
sum_result = first_number + second_number
difference_result = first_number - second_number
product_result = first_number * second_number

print("\nResults:")
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)

# Division and remainder require the second number
# to be different from zero.
if second_number != 0:
    quotient_result = first_number / second_number
    remainder_result = first_number % second_number

    print("Quotient:", quotient_result)
    print("Remainder:", remainder_result)
else:
    print("Quotient: Cannot divide by zero")
    print("Remainder: Cannot divide by zero")


# ============================================================
# EXERCISE 3: Temperature Converter
# ============================================================

print("\n===== TEMPERATURE CONVERTER =====")

# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit:.2f}°F")


# Fahrenheit to Kelvin
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

kelvin = (fahrenheit_input - 32) * 5 / 9 + 273.15

print(f"{fahrenheit_input}°F = {kelvin:.2f}K")


# ============================================================
# EXERCISE 4: Robot Sensor Monitor
# ============================================================

print("\n===== ROBOT SENSOR MONITOR =====")

# Collect robot information
robot_name = input("Enter Robot Name: ")
robot_id = input("Enter Robot ID: ")
sensor_name = input("Enter Sensor Name: ")

# Convert sensor values to floating-point numbers
sensor_reading = float(input("Enter Sensor Reading: "))
operating_limit = float(input("Enter Operating Limit: "))

# Calculate the difference between the limit and current sensor reading
difference = operating_limit - sensor_reading


# Display the sensor report
print("\n" + "=" * 40)
print("         ROBOT SENSOR REPORT")
print("=" * 40)

print(f"Robot Name       : {robot_name}")
print(f"Robot ID         : {robot_id}")
print(f"Sensor Name      : {sensor_name}")
print(f"Sensor Reading   : {sensor_reading}")
print(f"Operating Limit  : {operating_limit}")
print(f"Difference       : {difference}")

print("=" * 40)
