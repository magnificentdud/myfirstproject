n = int(input())
for i in range (n):
    x = str(input())
    sum = 0
    cnt = 0
    for j in list(x):
        if j == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)