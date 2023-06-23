#!/usr/bin/python3
"""a simple calculator
this is created as a personal project to test my skills
"""
import math


def calculator(a, op, b=None):
    symList = ["+", "-", "*", "/", "**", "root", "log", "sin", "cos", "tan"]

    if not isinstance(a, (int, float)):
        print(f"Invalid number {a}, please check the number and try again.")
        return

    if op not in symList:
        print("Please check the operating symbol (function) and try again.")
        return

    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        elif op == "**":
            return a ** b
        elif op == "root":
            return math.sqrt(a)
        elif op == "log":
            return math.log(a)
        elif op == "sin":
            return math.sin(a)
        elif op == "cos":
            return math.cos(a)
        elif op == "tan":
            return math.tan(a)

    except TypeError:
        print("Error: Missing or invalid value for the second number.")
        return

"""Prompt the user for input"""
a = float(input("Enter your first number: "))
op = input("Enter one of these (+, -, *, /, **, log, sin, cos, tan, root): ")
b_in = input("Enter the second number or leave blank if not applicable: ")

if b_in:
    b = float(b_in)
    solution = calculator(a, op, b)
else:
    solution = calculator(a, op)
print(f"The Result of what you entered is: {solution}")
