t = int(input("t:"))
for i in range(t):
    r, s = input().split()
    r = int(r)
    result = ""
    for i in s:
        result += int(r)*i
    print(result)
