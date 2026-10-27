#from arthmentic import result

num1 = int(input("enter first number :"))
operator = input("enter operator : +, -, *, /, %")
num2 = float(input("enter second number : "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    result=(num1 * num2)
    print(round(result,1))
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 % num2)