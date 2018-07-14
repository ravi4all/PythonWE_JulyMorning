min_range = int(input("Enter min range : "))
max_range = int(input("Enter max range : "))

for i in range(min_range, max_range+1):
    for j in range(2,i):
        if i % j == 0:
            # print("Not Prime",i)
            break
    else:
        print("Prime",i)