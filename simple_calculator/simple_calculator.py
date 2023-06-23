#!/usr/bin/python3
"""a simple calculator
this is created as a personal project to test my skills
"""
import math as d


a = input("Please input the first number: ")
op = input("Please enter the function you want to perform\
            + to add, - to subtract, * to multiply, / to divide,\
            ** to raise to power, | for square root: \n")
b = input("please input the second number: ")
a = float(a)
b = float(b)

symList = ["+", "-", "*", "/", "**", "|"]

if not isinstance(a, (int, float)):
    print(f"Invalid number {a}, please check the number and try again")
if not isinstance(b, (int, float)):
    print(f"Invalid number {b}, please try again")
if op not in symList:
    print("Please check the operating symbol(function) and try again")


if op == "+":
    print(a + b)
if op == "-":
    print(a - b)
if op == "*":
    print(a * b)
if op == "/":
    print(a / b)
if op == "**":
    print(a ** b)
if op == "|":
    print(d.sqrt(a), d.sqrt(b))

