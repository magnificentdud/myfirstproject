winner = 0
max_score = 0
for i in range(5):
    points = sum(list(map(int, input().split())))
    
    if points > max_score:
        max_score = points
        winner = i+1
print(winner, max_score)





