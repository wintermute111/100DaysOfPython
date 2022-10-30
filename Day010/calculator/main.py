from art import logo


def add(n1, n2):
    """Add n1 + n2 and return the result"""
    return n1 + n2


def subtract(n1, n2):
    """Subtract n1 - n2 and return the result"""
    return n1 - n2


def multiply(n1, n2):
    """Multiply n1 * n2 and return the result"""
    return n1 * n2


def divide(n1, n2):
    """Divide n1 / n2 and return the result"""
    return n1 / n2


def calculator():
    print(logo)
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    keep_going = "y"
    num1 = float(input("What is the first number? "))
    while keep_going == "y":
        for op in operations:
            print(op)
        operation = input("Pick an operation from the list above: ")
        num2 = float(input("What is the next number? "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        keep_going = input(f"Would you like to perform another operation on the answer {answer}? (y/n) ").lower()
        num1 = answer
        if keep_going == "n":
            calculator()


calculator()
