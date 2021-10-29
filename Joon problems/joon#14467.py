n = int(input())
cow = [-1] * 11
cnt = 0

for _ in range(n):
    target_cow, position = map(int, input().split())

    if cow[target_cow] == -1:
        cow[target_cow] = position
    else:
        if cow[target_cow] != position:
            cnt += 1
            cow[target_cow] = position

print(cnt)