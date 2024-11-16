# Addition Only Calculator Program

def addition_calculator():
    print("Welcome to the Addition Calculator!")
    
    # Get input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the addition
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the calculator
addition_calculator()
