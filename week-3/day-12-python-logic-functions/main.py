# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40

def calculate_grade(score):
    if score >= 70 and score <= 100:
        return "A"
    elif score >= 60 and score <= 69:
        return "B"
    elif score >= 50 and score <= 59:
        return "C"
    elif score >= 40 and score <= 49:
        return "D"
    else:
        return "F"
    


# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

def multiplication_table():
    keep_going = "yes"
    while keep_going == "yes":
        try:
            num = int(input("Enter a number for the multiplication table: "))
            print(f"--- Multiplication Table for {num} ---")
            for i in range(1, 13):
                print(f"{num} x {i} = {num * i}")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        
        keep_going = input("Do you want to calculate another? (yes/no): ").lower()


# — Exercise 3: Temperature Converter —
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    while True:
        print("\n--- PYTHON UTILITY MENU ---")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Temperature Converter")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            try:
                score = float(input("Enter your score (0-100): "))
                grade = calculate_grade(score)
                print(f"Your Grade is: {grade}")
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == "2":
            multiplication_table()
            
        elif choice == "3":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                result = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {result}°F")
            except ValueError:
                print("Error: Please enter a valid numerical temperature.")
                
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
