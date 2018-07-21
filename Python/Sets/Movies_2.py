movies = [
    {'actions' : ['avengers','terminator','baahubali',
                  'baby','300','saw'],
     'biopic' : ['sultan','dangal', 'MS Dhoni'],
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

commonMovies = list(user_1.intersection(user_2))
print("Similar Movies are",commonMovies)
action = 0
comedy = 0
biopic = 0
drama = 0

for category in movies:
    for movie in commonMovies:
        if movie in category['actions']:
            action += 1
        elif movie in category['comedy']:
            comedy += 1
        elif movie in category['biopic']:
            biopic += 1
        else:
            drama += 1

print("Action : {}, Comdey : {}, Drama : {}, Biopic : {}".format(action,comedy,drama,biopic))

x = movies[0]['biopic']
y = []

for i in range(len(commonMovies)):
    for j in range(len(x)):
        if commonMovies[i] in x:
            if x[j] not in commonMovies:
                print(x[j])