print('Calculator Program !')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    num1 = float(input('Enter first number : '))
    for i in operations:
        print(i)
    should_continue = True
    while should_continue:
        chose_operation = input('Enter the operation : ')
        num2 = float(input('Enter second number : '))

        chose_function = operations[chose_operation]
        answer = chose_function(num1, num2)

        print(f'{num1} {chose_operation} {num2} = {answer}')
        check = input('Do you want to continue? "y" or type "n" to start a new one or press any other key to exit ')
        if check == 'y':
            num1 = answer
        elif check == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False
            print('Thanks for Using This Program !')


calculator()
