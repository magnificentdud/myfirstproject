a = list(map(int, input().split()))
x = min(a)
while True:
    count = 0
    for i in a:
        if x % i == 0:
            count += 1
    if count >= 3:
        print(x)
        break
    else:
        x += 1
