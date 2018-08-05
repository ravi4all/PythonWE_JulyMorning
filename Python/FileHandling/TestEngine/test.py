file = open('questions.txt')
questions = file.readlines()

options = [
    ['skip','pass','continue','next'],
    ['R','C','B','ABC'],
    ['game','pygame','numpy','panda'],
    ['random','randint','randrange','sample'],
    ['w','w+','wb','w++']
]

answers = ['continue','ABC','pygame','random','w++']

counter = 0
rightAns = []
for i in range(len(questions)):
    print(questions[i])

    for e,opt in enumerate(options[i]):
        print("{}. {}".format(e+1,opt))

    ans = int(input("Answer 1/2/3/4: "))
    if answers[i] == options[i][ans-1]:
        # print("Right ans")
        counter += 1
    else:
        rightAns.append(answers[i])

print("Final Score: ",counter)
print("Right Answeres are",rightAns)

