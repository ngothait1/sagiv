import time

myName = input("What is your name: ")
print("Hello " + myName + ", nice to meet you")
print("This is a special calculator, I would need two numbers from you")
check_numbers = False
while not check_numbers:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if (num1.isdigit() and num2.isdigit()):
        num1 = int(num1)
        num1Parity = "even" if num1 % 2 == 0 else "odd"
        num2 = int(num2)
        num2Parity = "even" if num2 % 2 == 0 else "odd"
        check_numbers = True
    else:
        print("Invalid input, please enter valid integers for both numbers.")
print("Thank you for putting in your numbers, " + str(num1) + " and " + str(num2))
print("I can see that the first number is " + num1Parity)
print("and the second is " + num2Parity)
if num1Parity == num2Parity:
    print("So both numbers are " + num1Parity)
else:
    print("So one of them is even and one is odd")
myOpr = input("What operation would you like to perform? (+, -, *, /): ")
mySum = None
if myOpr == "+":
    mySum = num1 + num2
elif myOpr == "-":
    mySum = num1 - num2
elif myOpr == "*":
    mySum = num1 * num2
elif myOpr == "/":
    if num2 != 0:
        divInput = input("You have chosen to divide, should the result be an integer? (y/n)")
        while divInput not in ['y', 'n']:
            divInput = input("Invalid input. Please enter 'y' for integer division or 'n' for float division: ")
        if divInput == 'y':
             mySum = num1 // num2 
        else: mySum = num1 / num2
    else:
        print("Error: Division by zero not allowed - Number 2 is zero!")

else:
    print("Error: operator " + myOpr + " is not supported!")
print(str(num1) + " " + myOpr + " " + str(num2) + " = " + str(mySum)) if mySum is not None else print("An error has occured, please try again")
print("Thank you for using my calculator on " + time.ctime())
