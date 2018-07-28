# lambda - Anonymous Functions
# used to create functions at run time and destroy them
# immediately

# x = 10
# y = 12
# add = lambda x,y : x + y
# print(add(x,y))

temp = [34.5, 33.2, 30.9, 38.7, 28.9]
f = list(map(lambda c : 9/5 * c + 32, temp))
print("Converted Temp",f)