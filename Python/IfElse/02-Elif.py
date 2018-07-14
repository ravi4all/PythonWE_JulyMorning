import webbrowser
from datetime import datetime
import time

# IfElse ladder - if elif

chat = True

while chat:
    userMessage = input("Enter your message : ")

    if userMessage == 'hi':
        print("Hi")
    elif userMessage == 'bye':
        print("Bye")
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
