array = list(map(int, input().split()))

d = int(input())
n = []
for i in array:
    if i%d == 0:
        n.append(i)
    else:
        continue
print(n)