import random


player1 = ["rock", "paper", "scissors"]
player2 = ["rock", "paper", "scissors"]

x = random.choice(player1)
y = random.choice(player2)

print(x)
print(y)

if x == "rock" and y == "paper" or x == "paper" and y == "scissors" or x == "scissors" and y == "rock":
    print("player2 wins")
elif x == "rock" and y == "scissors" or x == "paper" and y == "rock" or x == "scissors" and y == "paper":
    print("player1 wins")
else:
    print("draw")
