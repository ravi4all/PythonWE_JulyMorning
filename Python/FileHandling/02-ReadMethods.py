file = open('data.txt')

# data = file.read()

# will read till 20th character
# data = file.read(20)

# will return line by line
# data = file.readline()

# will return list of all sentences seperated by new line
# data = file.readlines()

# will move cursor in the file to 40th index
pos = file.seek(40)
data = file.read()
print(data)

file.close()