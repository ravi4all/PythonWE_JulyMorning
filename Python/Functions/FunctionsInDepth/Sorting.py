# data = [2,4,5,7,2,4,6,8,8,4,12,45,33,7,56]

# by default sort in ascending order
# print(sorted(data))

# print(sorted(set(data), reverse=True))

# data = [
#     ['Ram',78], ['Shyam',87], ['Aman', 54],
#     ['Ishant',40], ['Kunal',33], ['Dhruv', 95]
# ]

data = [
    {'name':'Apple','price':60000},
    {'name':'Samsung','price':55000},
    {'name':'Vivo','price':25000},
    {'name':'Redmi','price':15000},
    {'name':'Nokia','price':20000}
]

# print(sorted(data, key = lambda x : x[1]))

print(sorted(data, key = lambda x : x['price']))