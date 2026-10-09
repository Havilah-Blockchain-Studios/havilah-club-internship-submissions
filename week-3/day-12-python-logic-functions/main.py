# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.

import math

# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40

def calculate_grade(score):
    # TODO: implement grade logic
    pass

# from 70 to 100 = A
# from 60 to 69 = B
# from 50 to 59 = C
# from 40 to 49 = D
# Below 40 = F

score = float(input("Enter your score(0-100): "))

if score >= 70:
    print ("Grade: A"),
elif score >= 60:
    print ("Grade: B"),
elif score >= 50:
    print ("Grade: C"),
elif score >= 40:
    print ("Grade: D"),
else:
    print ("Grade: F")


def grade_calculator():
    try:
        score = float(input("Enter your score(0 - 100): "))
    except ValueError:
        print("Invalid input. please enter a number.")
        return
    if score < 0 or score > 100:
        print("Score must be between 0 and 100")
        return
    print(f"Grade: {calculate_grade(score)}")
    
        

# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

# TODO: implement loop and table logic
    pass


def print_table(number):
    print(f"\n--- Multiplication Table for {number} ---")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")
    print("-" * 30 + "\n")
    
    
def multiplication_table():
    while True:
        user_input = input('Enter a number for the multiplication table (or type "quit" to exit): ').strip()
        if user_input.lower() == "quit":
            print("Returning to the main menu.\n")
        break
    try:
        number = int(user_input)
        print_table(number)
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'quit'.\n")

# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().


#_________________Area Calculator__________________#
def your_function():
    # TODO: implement your chosen function
    pass


import math

# Rectangle: length * width
def calculate_rectangle_area(length, width):
    return length * width

# Square: side * side
def calculate_square_area(side):
    return side ** 2

# Circle: pi * radius ** 2
def calculate_circle_area():
    return math.pi * radius ** 2

# Triangle: 0.5 * base * height
def calculate_triangle_area(base, height):
    return 0.5 * base * height


def area_calculator():
    print("---Area Calculator ---")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("3. Triangle")
    shape = input("choose a shape(1-4): ").strip()
    
    try:
        if shape == "1":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = calculate_rectangle_area(length, width)
            print(f"The area of the rectangle is: {area:.2f}")
        elif shape == "2":
            side = float(input("ENter the side length of the square: "))
            area = calculate_square_area(side)
            print(f"The area of the square is: {area:.2f}")
        elif shape == "3":
            radius = float(input("Enter the radius of the circle: "))
            are = calculate_circle_area(radius)
            print(f"The area of the circle is: {area:.2f}")
        elif shape == "4":
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = calculate_triangle_area(base, height)
            print(f"The area of the triangle is: {area:.2f}")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
    except ValueErrror:
        print("invalid input.Please enter a number.") 


# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():

    while True:
        print("=== MAIN MENU ===")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("4. Exit")
        
        choice = input("select an option(1-4): ").strip()
        
        if choice == "1":
            grade_calculator()
            
        elif choice == "2":
            multiplication_table()
            
        elif choice == "3":
            area_calculator()
        
        if choice == "4":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. please enter 1, 2, 3, or 4.\n")
            

# Run the program
if __name__ == "__main__":
    main()
