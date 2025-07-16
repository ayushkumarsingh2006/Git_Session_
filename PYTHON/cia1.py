import math

def calculator():
    while True:
        print("\n========== Calculator ==========")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Modulo (x % y)")
        print("7. Square Root (√x)")
        print("8. Exit")
        
        choice = input("Choose operation (1-8): ")

        if choice == '8':
            print("Exiting... Thank you!")
            break

        if choice == '7':
            x = float(input("Enter number: "))
            print("√", x, "=", math.sqrt(x))
            continue

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", x + y)
        elif choice == '2':
            print("Result:", x - y)
        elif choice == '3':
            print("Result:", x * y)
        elif choice == '4':
            if y == 0:
                print("Error! Division by zero.")
            else:
                print("Result:", x / y)
        elif choice == '5':
            print("Result:", x ** y)
        elif choice == '6':
            print("Result:", x % y)
        else:
            print("Invalid choice. Try again.")

# Run it
calculator
