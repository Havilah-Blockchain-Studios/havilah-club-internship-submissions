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


# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

def multiplication_table():
    # TODO: implement loop and table logic
    while True:
        number = input("Enter a number (or type 'quit' to stop): ")

        if number.lower() == "quit":
            break

        try:
            number = int(number)

            for i in range(1, 13):
                print(f"{number} x {i} = {number * i}")

        except ValueError:
            print("Please enter a valid number.")


# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

def your_function():
    # TODO: implement your chosen function
    text = input("Enter a word: ")

    if text.lower() == text.lower()[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")


# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    # TODO: build the menu here
    while True:
        print("\n=== Python Utility Menu ===")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Palindrome Checker")
        print("4. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                score = float(input("Enter your score (0-100): "))

                if 0 <= score <= 100:
                    print("Grade:", calculate_grade(score))
                else:
                    print("Score must be between 0 and 100.")

            elif choice == "2":
                multiplication_table()

            elif choice == "3":
                your_function()

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1-4.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
