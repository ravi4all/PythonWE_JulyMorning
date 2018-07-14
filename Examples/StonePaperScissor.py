import random
import time

options = ['stone','paper','scissor']

game = True

cpuScore = 0
userScore = 0

while game:
    userChoice = input("Enter your choice : ")
    time.sleep(1)
    cpu = random.choice(options)
    print("CPU -", cpu)
    if userChoice == cpu:
        print("Match Tie...")
        print("User : {}    CPU : {}".format(userScore,cpuScore))
    elif userChoice == 'stone' and cpu == 'paper':
        print("CPU Win")
        cpuScore += 1
        print("User : {}    CPU : {}".format(userScore, cpuScore))
    elif userChoice == 'paper' and cpu == 'scissor':
        print("CPU Win")
        cpuScore += 1
        print("User : {}    CPU : {}".format(userScore, cpuScore))
    elif userChoice == 'scissor' and cpu == 'stone':
        print("CPU Win")
        cpuScore += 1
        print("User : {}    CPU : {}".format(userScore, cpuScore))
    elif userChoice == 'stone' and cpu == 'scissor':
        print("You Win")
        userScore += 1
        print("User : {}    CPU : {}".format(userScore, cpuScore))
    elif userChoice == 'paper' and cpu == 'stone':
        print("You Win")
        userScore += 1
        print("User : {}    CPU : {}".format(userScore, cpuScore))
    elif userChoice == 'scissor' and cpu == 'paper':
        print("You Win")
        userScore += 1
        print("User : {}    CPU : {}".format(userScore, cpuScore))
    else:
        print("Invalid Input")


    if userScore == 5 or cpuScore == 5:
        print("Game Over")
        game = False