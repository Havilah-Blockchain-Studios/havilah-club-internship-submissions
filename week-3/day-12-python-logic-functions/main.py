# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40

def calculate_grade(score):
    if score >= 70:
        print("Grade A")
    elif score >= 60:
        print("Grade B")
    elif score >= 50:
        print("Grade C")
    elif score >= 40:
        print("Grade D") 
    else:
        print("GRADE 'F', YOU FAILED!!!") 
    pass

calculate_grade(int(input("Enter your score: ")))


# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

def multiplication_table(num):
    for multiplier in range(1, 13):
        result = num * multiplier
        print(num, "X", multiplier, "=", result)
    pass    

multiplication_table(int(input("Enter number: ")))

# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

def temp(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, "celsius converted to", fahrenheit, "fahrenheit")
    pass

temp(float(input("Enter temperature in celsius: ")))

# -- Function 4: Your Choice ---------------------------------------------------

try:
    age = int(input("Enter your age: "))
    print("You are", age, "years old")
except ValueError:
    print("Please enter a valid nuimber")
    

# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def calculate_grade(score):
    if score >= 70:
        print("Grade A")
    elif score >= 60:
        print("Grade B")
    elif score >= 50:
        print("Grade C")
    elif score >= 40:
        print("Grade D") 
    else:
        print("GRADE 'F', YOU FAILED!!!")  


def multiplication_table(num):
    for multiplier in range(1, 13):
        result = num * multiplier
        print(num, "X", multiplier, "=", result)    


def temp(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, "celsius converted to", fahrenheit, "fahrenheit")           


def select(option):
    if option == 1:
        calculate_grade(int(input("Enter your score: ")))
    elif option == 2:
        multiplication_table(int(input("Enter number: ")))
    elif option == 3:
        temp(float(input("Enter temperature in celsius: ")))


def main():
    print("Hello welcome to XELTECH utility app!!!")
    print("|press 1 for Grade calculator|", "|press 2 for Multiplication Table|", "|press 3 for Temperature converter|", "|press 0 to exit|")

    while True:
        try:
            choice = int(input("Select a tool(1, 2, 3, or 0 to exit): "))
        except ValueError:
            print("Please enter a valid number.") 

        if choice == 0:
             print("User logged out")
             break

        select(choice)


if __name__ == "__main__":
    main() 