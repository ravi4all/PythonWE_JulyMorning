# if file do not exist then it will create new file
file = open('data_2.txt','w')

# data = "hello this is file handling demo"

data = ["Ram","Shyam","Mohan","Gopal"]
for d in data:
    file.write(d+"\n")

file.close()