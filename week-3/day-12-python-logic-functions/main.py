# Day 12 — Python Logic and Functions


def calculate_grade(score):
        if score >= 70 :
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C"
        elif score >= 40:
            return "D"
        else:
            return "F"
        

def multiplication_table():
    while True:
        user_input = input("Enter a number (or type 'quit' to exit):")
        if user_input.lower()== "quit":
            break
        number = int(user_input)
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")
    


def your_function():
        celcius =float(input("Enter temperature in celcius:"))
        fahrenheit = (celcius * 9/5) + 32
        print(f"{celcius}°C is equal to {fahrenheit}°F")


def main():
    
     while True:
          print("\n--- Python Utility Menu ---")
          print("1. Grade Calculator")
          print("2. Multiplication Table")
          print("3. Temperature Converter")
          print("4. Exit")

          choice = input("Enter your choice (1-4): ")

          try:
              
              if choice == "1":
                  score = int(input("Enter a score(0-100):"))
                  print("Grade:", calculate_grade(score))
              elif choice == "2":
                  multiplication_table()
              elif choice == "3":
                  your_function()
              elif choice == "4":
                  print("Goodbye!")
                  break
              else:
                  print("Invalid choice. Please enter  a number between 1 and 4")
          except ValueError:
              print ( "Error: Please enter a valid number.")
                  

if __name__ == "__main__":
    main()
