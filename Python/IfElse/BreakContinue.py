# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)

# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)

for i in range(1,10):
    for j in range(1,5):
        if i == j:
            continue
        print("I is {} and J is {}".format(i,j))