a, b = map(int, input().split())
d = []
for i in range(1, a+1):
    if a % i == 0 and b % i == 0:
        d.append(i)
c = max(d)
e = a//c
f = b//c

print(c, e*f*c)

