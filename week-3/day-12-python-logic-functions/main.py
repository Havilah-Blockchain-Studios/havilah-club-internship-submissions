# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

def multiplication_table():
   while True:
        user_input = input("Enter a number for the multiplication table (or type 'quit' to exit): ").strip().lower()
        
        if user_input == 'quit':
            break
            
        try:
            number = float(user_input)
            print(f"\n--- Multiplication Table for {number} ---")
            for i in range(1, 13):
                result = number * i
                # Clean up display for whole numbers
                if number.is_integer():
                    print(f"{int(number)} x {i} = {int(result) if result.is_integer() else result}")
                else:
                    print(f"{number} x {i} = {result}")
            print("-" * 35 + "\n")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit'.\n")

# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

def your_function():
   while True:
        user_input = input("Enter a number for the multiplication table (or type 'quit' to exit): ").strip().lower()
        
        if user_input == 'quit':
            break
            
        try:
            number = float(user_input)
            print(f"\n--- Multiplication Table for {number} ---")
            for i in range(1, 13):
                result = number * i
                # Clean up display for whole numbers
                if number.is_integer():
                    print(f"{int(number)} x {i} = {int(result) if result.is_integer() else result}")
                else:
                    print(f"{number} x {i} = {result}")
            print("-" * 35 + "\n")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit'.\n")

# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    while True:
        user_input = input("Enter a number for the multiplication table (or type 'quit' to exit): ").strip().lower()
        
        if user_input == 'quit':
            break
            
        try:
            number = float(user_input)
            print(f"\n--- Multiplication Table for {number} ---")
            for i in range(1, 13):
                result = number * i
                # Clean up display for whole numbers
                if number.is_integer():
                    print(f"{int(number)} x {i} = {int(result) if result.is_integer() else result}")
                else:
                    print(f"{number} x {i} = {result}")
            print("-" * 35 + "\n")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit'.\n")


if __name__ == "__main__":
    main()
