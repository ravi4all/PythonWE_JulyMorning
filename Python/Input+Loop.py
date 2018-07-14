num = int(input("Enter the number : "))

# range(start,stop,step)
# start - by default = 0

# indentation - by default - 4 spaces
#for i in range(10,20):
#    print(i*num)

for i in range(1,11):
    print("{} x {} = {}".format(num,i,i*num))
    print("--------")

print("End of table")
