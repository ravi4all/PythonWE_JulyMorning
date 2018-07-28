def isEven(num):
    return num % 2 == 0

numbers = [i for i in range(1,101)]

e = list(filter(isEven, numbers))
print(e)