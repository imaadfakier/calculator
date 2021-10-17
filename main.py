from art import logo


# addition
def add(n1, n2):
    return n1 + n2


# subtraction
def subtract(n1, n2):
    return n1 - n2


# multiplication
def multiply(n1, n2):
    return n1 * n2


# division
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)

    keep_calculating = 'y'

    # num1 = int(input('What\'s the first number?: '))
    num1 = float(input('What\'s the first number?: '))

    for operation in operations:
        print(operation)

    while keep_calculating == 'y':
        operation_symbol = input('Pick an operation: ')

        # num2 = int(input('What\'s the next number?: '))
        num2 = float(input('What\'s the next number?: '))

        answer = operations[operation_symbol](num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        num1 = answer

        keep_calculating = input(f"Type 'y' to continue calculating with {answer},\nType 'n' to start a new calculation.:,\nOr type 'e' to exit.: ")
    else:
        if keep_calculating == 'n':
            calculator()


calculator()

# final takeaway: always aim to make your code as reusuable
# and modular as possible as these are best practices when
# programming, in general