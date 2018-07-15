# user defined function

# global scope
x = 12
y = 15

def add():
    # local scope
    x = 10
    y = 12
    z = x + y
    print("Sum is",z)

add()
print(x - y)