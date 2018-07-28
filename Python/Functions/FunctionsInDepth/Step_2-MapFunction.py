def tempConv(c):
    # c = 45.6
    return 9 / 5 * c + 32

temp = [34.5, 33.2, 30.9, 38.7, 28.9]

# f = list(map(tempConv, temp))
# print("Converted Temp",f)

def myMap(func, iter):
    outcome = []
    for i in range(len(iter)):
        outcome.append(func(iter[i]))

    return outcome

f = myMap(tempConv, temp)
print("Converted Temperatures",f)