numbers = [i for i in range(1,101)]
e = list(filter(lambda num : num % 2 == 0, numbers))
print(e)