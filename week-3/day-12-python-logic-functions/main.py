# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# EXERCISE 1: GRADE CALCULATOR

def calculate_grade(score):

# Calculates the grade and gives remark for a score.
    if score >= 70:
        return "A", "Excellent"
    elif score >= 60:
        return "B", "Very Good"
    elif score >= 50:
        return "C", "Good"
    elif score >= 40:
        return "D", "Pass"
    else:
        return "F", "Fail"


def grade_calculator():

# Collects course information and display the grade report.
    course_code = input("Enter Your Course Code: ")

    while True:
        try:
            score = float(input("Enter Your Score (0-100): "))

            if 0 <= score <= 100:
                break

            print("Invalid score. Please enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a numerical score.")
            print("Example: 75")

    grade, remark = calculate_grade(score)

    print("\n" + "=" * 40)
    print("             GRADE REPORT")
    print("=" * 40)
    print(f"Course Code : {course_code}")
    print(f"Score       : {score}")
    print(f"Grade       : {grade}")
    print(f"Remark      : {remark}")
    print("=" * 40)


# EXERCISE 2: MULTIPLICATION TABLE

def multiplication_table():

# Displays a multiplication table from 1 to 12.
    while True:
        try:
            number = int(input("\nEnter a whole number: "))

            print(f"\n===== MULTIPLICATION TABLE FOR {number} =====")

            for multiplier in range(1, 13):
                result = number * multiplier
                print(f"{number} x {multiplier} = {result}")

        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        another_calculation = input(
            "\nDo you want another multiplication table? (yes/no): "
        ).strip().lower()

        if another_calculation != "yes":
            break


# EXERCISE 3: TEMPERATURE CONVERTER

def celsius_to_fahrenheit(celsius):
# Convert Celsius to Fahrenheit and returns the result.
    fahrenheit = (celsius * 9 / 5) + 32

    return fahrenheit


def temperature_converter():

# Gets Celsius input and displays the Fahrenheit result.
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))

            fahrenheit = celsius_to_fahrenheit(celsius)

            print(f"\n{celsius:g}°C = {fahrenheit:.2f}°F")
            break

        except ValueError:
            print(
                "Invalid input. Please enter a numerical temperature."
            )


# EXERCISE 4: ERROR HANDLING

# Numerical inputs throughout the program are protected
# with try/except blocks to handle ValueError.


# EXERCISE 5: PYTHON UTILITY MENU

def main():

# Displays the utility menu and runs the selected option.
    while True:
        print("\n" + "=" * 40)
        print("          BBDH UTILITY TOOLS MENU")
        print("=" * 40)
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Temperature Converter")
        print("4. Exit")
        print("=" * 40)

        choice = input("Choose an option from (1-4): ").strip()

        if choice == "1":
            grade_calculator()

        elif choice == "2":
            multiplication_table()

        elif choice == "3":
            temperature_converter()

        elif choice == "4":
            print("\nThank you for using the BBDH Utility Tools.")
            break

        else:
            print(
                "\nInvalid choice. "
                "Please select an option from 1 to 4."
            )


# PROGRAM START

if __name__ == "__main__":
    main()