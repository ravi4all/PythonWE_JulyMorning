def tempConv(c):
    return 9 / 5 * c + 32

temp = [34.5, 33.2, 30.9, 38.7, 28.9]

# tempConv(temp[0])

f = []
for t in temp:
    f.append(tempConv(t))

print("Converted Temp",f)