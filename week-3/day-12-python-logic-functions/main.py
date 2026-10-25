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
        user_input = input("\nEnter a number for its multiplication table (or 'quit'): ")
        if user_input.lower() == "quit":
        print("Returning to main menu...")

     break
        try:
            number = int(user_input)
            print(f"\nMultiplication Table for {number}")
            for i in range(1, 13):
                print(f"{number} x {i} = {number * i}")
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")


# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

        def your_function():

    text = input("\nEnter a word or phrase: ")
    cleaned_text = text.replace(" ", "").lower()

    if cleaned_text == cleaned_text[::-1]:
        print("This is a palindrome.")
        
    else:
         print("This is not a palindrome.")


# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    while True:
        print("\n  PYTHON UTILITY MENU  ")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Palindrome Checker")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            try:
                score = float(input("\nEnter your score (0-100): "))
                if 0 <= score <= 100:
                    grade = calculate_grade(score)
                    print(f"Grade: {grade}")

                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            multiplication_table()

        elif choice == "3":
            your_function()

        elif choice == "4":
            print("Goodbye!")

            break

        else:
            print("Invalid choice. Please select an option from 1 to 4.")

if __name__ == "__main__":

    main()

