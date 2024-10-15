
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))  # Convert input to integer
        except ValueError:
            print("Invalid input. Please enter a WHOLE number.")

def get_operator():
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in ('+', '-', '*', '/'):
            return operator
        else:
            print("Invalid operator. Please enter one of +, -, *, /.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b  # Floating-point division
    else:
        print("Error: Division by zero.")
        return None

def main():
    print("I am the Big Brain. Master of all knowledge")
    number_1 = get_number("Please give me your first number: ")
    operator = get_operator()
    number_2 = get_number("Please give me your second number: ")

    if operator == '+':
        operator_name = "plus"
        result = add(number_1, number_2)
    elif operator == '-':
        operator_name = "minus"
        result = subtract(number_1, number_2)
    elif operator == '*':
        operator_name = "times"
        result = multiply(number_1, number_2)
    elif operator == '/':
        operator_name = "divided by"
        result = divide(number_1, number_2)

    if result is not None:
        print(f"The Big Brain says \"{number_1} {operator_name} {number_2} is {result}\"")

main()
