# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40

    #TODO:

def grade_calculator():
  while True: 
     try: 
      score = int(input("Enter your score"))
      break
     except ValueError:
       print("Invalid input. Please enter a valid score.")
       continue 
  if score >= 70:
        print("You scored an A")
  elif score >= 60:
        print("You scored a B")
  elif score >= 50:
        print("You scored a C")
  elif score >= 40:
        print("You scored a D")
  else:
        print("You failed woefully")
        
grade_calculator()  


# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.


    # TODO: implement loop and table logic
def multiplication_table():
 while True:
    try:  
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    for multiplier in range(1, 13):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")

    again = input("Do you want to do another calculation? (yes/no): ")
    if again.lower() != "yes":
            break
multiplication_table()

    
# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

#TODO: calculate the area of a rectangle given its length and width. 
# def Calculate_area():
def Calculate_area():
    while True:
        try:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    area = length * width
    print("The area of the rectangle is:", area)

Calculate_area()

# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Calculate Area of Rectangle")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            grade_calculator()
        elif choice == '2':
            multiplication_table()
        elif choice == '3':
            Calculate_area()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
main_menu()