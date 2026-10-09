# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40
def calculate_grade(score):
    if score >= 70:
       print("A")
    elif score >= 60:
      print("B")
    elif score >= 50:
     print("C")
    elif score >= 45:
     print("D")
    elif score >= 40:
     print("E")
    else:
     print("F")


# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

def multiplication_table():
    # TODO: implement loop and table logic
    num = int(input("Enter a number: "))

    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")


# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

def your_function():
    length = int(input("enter the length:  "))
    width = int(input("enter the width:    "))

    Area = length * width
    print(Area)

# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    while True:
        print("\nMenu:")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Your Function")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            calculate_grade()
        elif choice == '2':
            multiplication_table()
        elif choice == '3':
            your_function()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
