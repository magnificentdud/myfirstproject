import random
import time
words = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf", "pizza", "book", "papa", "mama", "holala", "woochan", "Hellooo"]


# end = time.time()
# totaltime = start - end
n = 1
while n <6:
    start = time.time()
    y = (random.choice(words))
    print(y)
    x = input()

    end = time.time()
    totaltime = end - start

    if x == y and totaltime < 2.5:
        print("nice job")
        print(totaltime)
    elif totaltime > 2.5 and x == y:
        print("nice try but too late")
    elif y != x and totaltime<2.5:
        print("wrong answer")
    elif y!=x and totaltime>2.5:
        print("BABO")
n +=1
