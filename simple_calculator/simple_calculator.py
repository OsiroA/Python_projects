#!/usr/bin/python3
"""a simple calculator
this is created as a personal project to test my skills
"""
import math as d


a = input("Please input the first number: ")
op = input("Please enter the function you want to perform\
            + to add, - to subtract, * to multiply, / to divide,\
            ** to raise to power, | for square root")
b = input("please input the second number: ")


symList = ["+", "-", "*", "/", "**", "|"]

if type(a) != int or type(a) != float:
    print("Invalid number {a}, please check the number and try again")
if type(b) != int or type(b) != float:
    print("Invalid number {b}, please try again")
if op not in symList:
    print("Please check the operating symbol(function) and try again")


if op == "+":
    return a + b
if op == "-":
    return a - b
if op == "*":
    return a * b
if op == "/":
    return a / b
if op == "**":
    return a ** b
if op == "|":
    return d.sqrt(a), d.sqrt(b)

