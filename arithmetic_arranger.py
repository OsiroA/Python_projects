def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  arranged_problems = ''
  first_line = ''
  second_line = ''
  dash_line = ''
  result_line = ''
#show_answers_line = ''

  #loop through each problem(wahala)
  for wahala in problems:
    n1, symbol, n2 = wahala.split()
    #check validity according to question requirements
    if not (n1.isdigit() and n2.isdigit()):
      return "Error: Numbers must only contain digits."
    if ((len(n1) > 4) | len(n2) > 4):
      return "Error: Numbers cannot be more than four digits."
    if symbol not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
    #calculate the width of the problem
    width = max(len(n1), len(n2))
    #2 is added to represent the space for symbol an the space between it and the longer operand
    #next line creates the first line
    first_line = n1.rjust(width)

    #create the second line
    #we deduct two because we added it to the width ten for the length of the first operand
    second_line = n2.rjust(width - 2) + "  "

    #create the dash line
    dash_line += "-" * width + "  "

    #calculate the result
    result = str(eval(wahala))

    #concatenate the lines for final outputs
    #arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip(
    # ) + '\n' + dash_line.rstrip()
    #result_line = result.rjust(width) + "    "  #creating the answer line
    #add the answer line
    if show_answers:
      arranged_problems += result_line.rstrip()

  #print("actual output:", actual)
  #print("expected output:", expected_output)
    return arranged_problems
