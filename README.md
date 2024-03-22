# Python_projects
This repository is for projects I do in the python class organized by freecodecamp.org

README.md for arithmetic_arranger Function
HGHF
The arithmetic_arranger() function takes in a list of arithmetic problems in the form of strings and returns a formatted string that arranges the problems vertically.

Inputs

problems (required) : A list of arithmetic problems. Each problem should be a string and should be formatted with a single operator (either '+' or '-') separating two operands. Each operand should contain only digits and should be no more than four digits long. There should be no spaces within operands. Example: ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
show_answers (optional) : A boolean value that determines whether the function should show the answers to the arithmetic problems. If set to True, the function will display the answer to each problem below the dash line. If set to False (default), the function will only display the problem and the dash line.
Outputs

Returns a string that contains the formatted arithmetic problems.
If there are more than five problems in the problems list, the function will return an error message: Error: Too many problems.
If an operand in any problem contains a character that is not a digit, the function will return an error message: Error: Numbers must only contain digits.
If an operand in any problem is more than four digits long, the function will return an error message: Error: Numbers cannot be more than four digits.
If an operator in any problem is not '+' or '-', the function will return an error message: Error: Operator must be '+' or '-'.

from arithmetic_arranger import arithmetic_arranger

# Example 1: Displaying only problems and dash line
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))
# Output:
#   32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----

# Example 2: Displaying problems, dash line, and answers
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems, show_answers=True))
# Output:
#   32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----
#  730      3799      88      172


Limitations

The function only works with arithmetic problems that have single-digit operators.
The function only works with arithmetic problems that have two operands.
The function only works with addition and subtraction operators.
