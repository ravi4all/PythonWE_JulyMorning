import webbrowser
from datetime import datetime
import time
import random

helloIntent = ['hi','hello','hey','wass up','hey there']
byeIntent = ['bye','bie','take care','see you']

chat = True

while chat:
    userMessage = input("Enter your message : ")
    if userMessage in helloIntent:
        cpuMessage = random.choice(helloIntent)
        print(cpuMessage)
    elif userMessage in byeIntent:
        cpuMessage = random.choice(byeIntent)
        print(cpuMessage)
        chat = False
    elif userMessage == 'open google':
        print("Welcome to google......")
        webbrowser.open('https://www.google.com')
    elif userMessage == 'tell me date':
        print("Please wait...")
        time.sleep(1)
        date = datetime.now().date()
        print(date)
    elif userMessage == 'tell me time':
        print("Please wait...")
        time.sleep(1)
        t = datetime.now().time()
        print(t)
    else:
        print("I don't understand")
