a = 25
primeNum = True
for i in range(2,a):
    if a % i == 0:
        # print("Not Prime")
        primeNum = False
        break
    else:
        primeNum = True
        # print("Prime Number")

if primeNum:
    print("Prime Number")
else:
    print("Not Prime")