
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed."


def modulus(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error! Modulus by zero is not allowed."


def simple_calculator():
    print("Welcome to the Python Simple Calculator!")

    while True:

        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")

        
        select_option = input("Enter Select (1/2/3/4/5/): ")


        if select_option in ['1', '2', '3', '4', '5']:
            try:
                
                number_one = float(input("Enter the first number: "))
                number_two = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue

           
            if select_option == '1':
                print(f"Addition: {number_one} + {number_two} = {add(number_one, number_two)}")

            elif select_option == '2':
                print(f"Subtraction: {number_one} - {number_two} = {subtract(number_one, number_two)}")

            elif select_option == '3':
                print(f"Multiplication: {number_one} * {number_two} = {multiply(number_one, number_two)}")

            elif select_option == '4':
                result = divide(number_one, number_two)
                print(f"Division: {number_one} / {number_two} = {result:.2f}")

            elif select_option == '5':
 
                print(f"Modulus: {number_one} % {number_two} = {modulus(number_one, number_two)}")
        else:
            print("Invalid select! Please select a valid option.")




simple_calculator()
