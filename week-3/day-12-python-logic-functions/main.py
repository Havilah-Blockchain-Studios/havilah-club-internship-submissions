# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40

def calculate_grade(score):
    # TODO: implement grade logic
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
    for score in test_scores:
        grade = calculate_grade(score)
        print(f"Score: {score} => Grade: {grade}")  



# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.
def multiplication_table():
    """Exercise 2: Multiplication Table"""
    while True:
        try:
            num = int(input("Enter a number to display its multiplication table: "))
            print(f"\nMultiplication Table for {num}:")
            for i in range(1, 13):
                print(f"{num} x {i} = {num * i}")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        choice = input("\nWould you like to generate another table? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting multiplication table generator.")
            break
        # Example usage: call multiplication_table() from the main menu.

# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

def your_function():
    # TODO: implement your chosen function
    def celcius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    #example usage:
    celsius_temp = 25
    print(f"{celsius_temp}°C is equal to {celcius_to_fahrenheit(celsius_temp)}°F")


    #Exercise 4: Error Handling: Add `try` / `except` to handle cases where the user enters text instead of a number. 
    #TODO: implement error handling
    # Exercise 4: Error Handling
def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")                 



# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    # TODO: build the menu here
    while True:
        print("\nMenu:")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Your Function")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            score = get_valid_number("Enter a score (0-100): ")
            grade = calculate_grade(score)
            print(f"Score: {score} => Grade: {grade}")
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
