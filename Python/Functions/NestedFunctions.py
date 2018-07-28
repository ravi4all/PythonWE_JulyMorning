def calc():
    x = 10
    y = 12

    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z

    # when we return multiple values we will get tuples
    return add, sub

# print(calc())
# x = calc()
# print(x())

def show():
    x = calc()
    # print(x)
    # print(x[0]())
    add = x[0]
    print(add())

show()