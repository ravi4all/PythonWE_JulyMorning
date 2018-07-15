movies = [
    {'actions' : ['avengers','terminator','baahubali',
                  'baby','300','saw'],
     'biopic' : ['sultan','dangal'],
     'comedy' : ['fukrey','3 idiots','pk'],
     'drama' : ['identity','seven','ghajini','jumanji']
     }
]

user_1 = {'avengers','terminator','baahubali',
          'sultan','jumanji','dangal','fukrey',
          'baby','seven','identity'}

user_2 = {'baahubali','dangal','jumanji','300','sultan',
          'fukrey','seven','ghajini','3 idiots',
          'avengers'}

numer = len(user_1.intersection(user_2))
denom = len(user_1.union(user_2))

j = numer / denom * 100

print("Similarity Score is",j,"%")

user_1_recommendation = user_2 - user_1
user_2_recommendation = user_1 - user_2

print("Movies recommended for user_1",user_1_recommendation)
print("Movies recommended for user_2",user_2_recommendation)