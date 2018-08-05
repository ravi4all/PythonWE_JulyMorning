import urllib.request

webpage = urllib.request.urlopen('https://www.google.co.in')
# print(webpage)
data = webpage.read()
with open('google.html','wb') as file:
    file.write(data)