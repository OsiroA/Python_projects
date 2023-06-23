#!/usr/bin/python3
"""a simple calculator
this is created as a personal project to test my skills
"""
import math


def calculator(a, op, b=None):
    symList = ["+", "-", "*", "/", "**", "|", "log"]

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
        elif op == "|":
            return math.sqrt(a)
        elif op == "log":
            return math.log(a)

    except TypeError:
        print("Error: Missing or invalid value for the second number.")
        return
