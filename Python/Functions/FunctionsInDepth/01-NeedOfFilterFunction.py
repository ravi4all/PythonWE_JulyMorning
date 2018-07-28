e = []
def isEven(num):
    if num % 2 == 0:
        e.append(num)
        # return num

numbers = [i for i in range(1,101)]

# print(isEven(12))
for n in numbers:
    # print(isEven(n))
    # if isEven(n):
    #     print(n)
    isEven(n)

print(e)
