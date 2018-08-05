import csv

# file = open('data.csv')
# file.close()

with open('data.csv') as file:
    reader = csv.reader(file)

    for data in reader:
        print(data)

# print(file.read())