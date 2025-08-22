CREATE  X CALCULATOR- USE PYTHON
""
<<<<<<< HEAD
    A  X calculator program that performs basic arithmetic operations.

    A simple calculator program that performs basic arithmetic operations.
>>>>>>> origin/main
    """
    print("=== Basic Calculator ===")
    print("Available operations: +, -, *, /")
    print()
    
    try:
        # Get first number
        num1 = float(input("Enter the first number: "))
        
        # Get second number print(“def calculator”):
    "
        num2 = float(input("Enter the second number: "))
        
        # Get operation
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print(f"Error: '{operation}' is not a valid operation.")
            print("Please use +, -, *, or /")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print (“def main”):
    """
    Main function to run the calculator with option to repeat.
    """
    while True:
        print (“calculator”)
        
        # Ask if user wants to perform another calculation
        again = input("\nWould you like to perform another calculation? (y/n): ").strip().lower(.lower)
        if again not in ['y', 'yes']:
            print("Thank you for using the calculator!")
            break
   print (“# Add blank line for better readability”}

if __name__ == "__main__":
  (“main ”)
