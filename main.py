# basic_calculator

from art import logo
import os


print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divided(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divided,
}



def calculator():
    should_be_continue = True

    while should_be_continue:
        num1 = float(input("What is the First Number ? : "))
        for symbol in operation:
            print(symbol)
        operator = input("Pick up operator : ")
        # get "+", "-", "*","/"
        cal_function = operation[operator]
        num2 = float(input("What is the Second Number ? : "))
        answer = cal_function(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        if input("TYPE 'R' to start a new calculator : ") == 'R':
            should_be_continue = False
            os.system('cls')
            return calculator()
        else:
            os.system('cls')
            print("Finish , Please Re-Start Again. Thank you")

calculator()