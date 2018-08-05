import csv

data = [
    ["Sachin Tendulkar","Batsman"],
    ["Virat Kohli","Batsman"],
    ["Yuvraj Singh","All-rounder"],
    ["MS Dhoni","WK/Batsman"],
    ["Md. Shami","Bowler"],
    ["Umesh Yadav","Bowler"]
]

with open('data.csv','w', newline='') as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)