# Day 12 - Python Logic & Functions
# Mbamalu Samuel Oluebubechukwu

# Exercise 1: Grade Calculator
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


# Exercise 2: Multiplication Table
def multiplication_table():
    while True:
        user_input = input("Enter a number (or 'quit' to stop): ")
        if user_input.lower() == "quit":
            break

        try:
            number = int(user_input)
        except ValueError:
            print("That's not a valid number. Try again.")
            continue

        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")


# Exercise 3: Palindrome Checker
def check_palindrome():
    text = input("Enter a word or phrase to check: ")
    cleaned = text.lower().replace(" ", "")
    if cleaned == cleaned[::-1]:
        print(f"'{text}' is a palindrome.")
    else:
        print(f"'{text}' is not a palindrome.")


# Main Menu
def main():
    while True:
        print("\n----- MENU -----")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Palindrome Checker")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        try:
            if choice == "1":
                score = int(input("Enter a score (0-100): "))
                print(f"Grade: {calculate_grade(score)}")
            elif choice == "2":
                multiplication_table()
            elif choice == "3":
                check_palindrome()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1-4.")
        except ValueError:
            print("Invalid input. Please enter a number where expected.")


if __name__ == "__main__":
    main()
