# Day 11 — Introduction to Python

student_name = "KOSISOCHUKWU"

student_age = 26

GPA = 4.0

in_partnership_with_havilah_club = True

print("Name:", student_name, "|Type:", type (student_name))

print("Age:", student_age,  "|Type:", type(student_age))

print("GPA:" ,GPA, "|Type:", type(GPA))

print("in partnership with havilah club:", in_partnership_with_havilah_club, "|Type:", type(in_partnership_with_havilah_club))


celcius = float(input("Enter temperature in Celsius:"))

fahrenheit = (celcius * 9/5) + 32

print("temperature in Fahrenheit:", fahrenheit )

fahrenheit_input = float(input("Enter temperature in Fahrenheit:"))

celcius_converted = (fahrenheit_input -32) * 5/9

print("Temperature in celcius:", celcius_converted )


name = input("Enter your name:")

birth_year = int(input("Enter your birth year:"))

current_year = 2026

age = current_year - birth_year

year_turning_30 = birth_year + 30
print("Hello", name + ", you are", age, "years old,")
print("you will turn 30 in the year :", year_turning_30)

a = 30
b = 45
print(a+b)
print(b-a)
print(a*b)
print(b/a) 

robot_name = "HavilahBot-Alpha"
robot_id = "HB-2026-X1"
sensor_name = "Thermal Tracker"

sensor_reading = 42.8

operatinglimit = 50.0
print("--- ROBOT SENSOR MONITOR REPORT ---")
print(f"Robot Name     : {robot_name}")
print(f"Robot ID       : {robot_id}")
print(f"Sensor Name    : {sensor_name}")
print(f"Current Reading: {sensor_reading}")
print(f"operating Limit: {operatinglimit}")

num1 = float(input("Enter the firt number:"))
num2 = float(input("Enter the secount number"))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print("Remainder:", num1 % num2)

robot_name = input("Enter Robot Name:")
robot_id = input("Enter Robot ID:")

sensor_name = input("Enter Sensor Name:")
sensor_reading = float(input("Enter Sensor Reading:"))
operation_limit = float(input("Enter Operation Limit:"))

difference = operation_limit - sensor_reading 

print("----- Robot Sensor Report -----")
print("Robot Name:", robot_name)
print("Robot ID:", robot_id)
print("Sensor Name:", sensor_name)
print("Sensor Reading:", sensor_reading)
print("Operating Limit:", operation_limit)
print("Difference (Limit - Reading):", difference)