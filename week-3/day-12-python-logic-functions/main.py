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
        user_input = input("Enter a number (or type 'quit' to stop): ").strip()
        if user_input.lower() == 'quit':
            break
        try:
            num = float(user_input)
            for i in range(1, 13):
                print(f"{num} x {i} = {num * i}")
        except ValueError:
            print("Invalid input! Please enter a number or 'quit'.")




# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

def check_palindrome():
    # TODO: implement your chosen function
    user_input = input("Enter a word or sentence to check for a palindrome: ".strip())
    cleared_output= "".join(user_input()).lower()

    if cleaned_input == cleaned_input[::-1]:
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is NOT a palindrome.")


# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    # TODO: build the menu here
    def main():
    while True:
        print("\n--- MENU ---")
        print("1. Grade Calculator\n2. Multiplication Table\n3. Palindrome Checker\n4. Exit")
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            score = input("Enter a score (0-100): ").strip()
            # A quick check to see if the input is a valid number
            if score.replace('.', '', 1).isdigit():
                print(f"Grade: {calculate_grade(float(score))}")
            else:
                print("Invalid input! Please enter a number.")
                
        elif choice == "2":
            multiplication_table()
            
        elif choice == "3":
            check_palindrome()
            
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please pick 1, 2, 3, or 4.")



if __name__ == "__main__":
    main()
