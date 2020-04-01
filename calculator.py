import re

print("Simple Calculator\nCreated by regux.com")
print("Type q to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(previous)
    if equation == "q":
        print("Good Bye.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performMath()
