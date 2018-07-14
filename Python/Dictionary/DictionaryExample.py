products = [
    {'id':101,'category':'shoes','brand':'Adidas','price':2000},
    {'id':102,'category':'mobile','brand':'Apple','price':40000, 'type':'iphone 7s'},
    {'id':103,'category':'shirt','brand':'TH','price':3500, 'color':'white'},
    {'id': 104, 'category': 'mobile', 'brand': 'Samsung', 'price': 45000, 'type': 'galaxy S5'},
    {'id':105,'category':'shoes','brand':'Nike','price':3000},
    {'id': 106, 'category': 'shirt', 'brand': 'PA', 'price': 3500, 'color': 'black'},
    {'id': 107, 'category': 'mobile', 'brand': 'Apple', 'price': 80000, 'type': 'iphone 8'},
    {'id':108,'category':'shoes','brand':'Puma','price':3800},
    {'id': 109, 'category': 'mobile', 'brand': 'Xiaomi', 'price': 15000, 'type': 'Redmi Note 4'},
    {'id': 110, 'category': 'shirt', 'brand': 'TH', 'price': 2500, 'color': 'black'},
    {'id':111,'category':'shoes','brand':'Adidas','price':4000},
    {'id':112,'category':'shoes','brand':'Nike','price':4000},
    {'id': 113, 'category': 'mobile', 'brand': 'Samsung', 'price': 20000, 'type': 'Note 2'},
]

print("""
Shoes | Mobile | Shirt
""")

toSearch = input("Enter your search : ")

for data in products:
    if data['category'] == toSearch.lower():
        print(data)
