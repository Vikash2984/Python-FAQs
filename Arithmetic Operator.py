#First_operand_input
num1 = int(input("\nEnter a Number       : "))

#Second_operand_input
op = input("Enter an operator (+, -, *, **, /, //, %) : ")

#Operator_operand_input
num2 = int(input("Enter another Number : "))

#Conditional_Statements_&_Output
if op == "+":
    print("Answer :",num1 + num2 )
elif op == "-":
    print("Answer :",num1 - num2 )
elif op == "*":
    print("Answer :",num1 * num2 )
elif op == "**":
    print("Answer :",num1 ** num2 )
elif op == "/":
    print("Answer :",num1 / num2 )
elif op == "//":
    print("Answer :",num1 // num2 )
elif op == "%":
    print("Answer :",num1 % num2 )
