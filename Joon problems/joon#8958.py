n = int(input())
for i in range(n):
    a = input()
    score = 0
    for j in a :
        if j == '0':
            score += 1
    print(score)
    
