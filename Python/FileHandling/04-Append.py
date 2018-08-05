file = open('data_2.txt','a')

data = ["John","Smith","Tom"]
for d in data:
    file.write(d+"\n")

file.close()