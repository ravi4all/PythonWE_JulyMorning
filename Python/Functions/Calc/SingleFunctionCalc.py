def calculator(x, y, opr):
    expression = x + opr + y
    # expression = '12' + '+' + '23'
    # expression = '12 + 23'
    # print(expression)
    # evaluate
    result = eval(expression)
    print("Result is",result)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

userInput = input("Enter your choice : ")

num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

operations = {
    "1" : "+",
    "2" : "-",
    "3" : "/",
    "4" : "*"
}

opr = operations.get(userInput)
calculator(num_1, num_2, opr)