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
    pass

def multiplication_table():
    number = int(input("Enter a number: "))

    for i in range(1, 13):
        print(number, "x", i, "=", number * i)

# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

def your_function():
    pass
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    pass
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Please enter a valid number.")

def main():
    while True:
        print("\nPython Utility Menu")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Temperature Converter")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            score = float(input("Enter your score: "))
            print("Grade:", calculate_grade(score))

        elif choice == "2":
            multiplication_table()

        elif choice == "3":
            celsius = float(input("Enter temperature in Celsius: "))
            print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
