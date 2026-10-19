# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# Exercise 1: Grade Calculator 

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


# Exercise 2: Multiplication Table 

def multiplication_table(num):
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num} *{i} = {num * i}")


# Exercise 3: Temperature Converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# Exercise 4: Safe Numerical Input (Error Handling)
def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


# Exrcise 5: Main Utility Menu
def main():
    while True:
        print("\n=== PYTHON UTILITY MENU ===")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Temperature Converter")
        print("4. Exit")

        choice = input("Select an option (1-4): ".strip())

        if choice == '1':
            score = get_number_input("Enter student score (0-100): ")
            if 0 <= score <= 100:
                grade = calculate_grade(score)
                print(f"Calculated Grade: {grade}")
            else:
                print ("Score must between 0 and 100.")

        elif choice == '2':
            num = get_number_input("Enter a number")
            multiplication_table(num)

        elif choice == '3':
            celsius = get_number_input("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}℃ is equal to {fahrenheit}℉")

        elif choice == '4':
            print("Exiting utility program. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose an option from 1 to 4.")


if __name__ == "__main__":
    main()