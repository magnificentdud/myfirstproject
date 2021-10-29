a = input()
b = input()

cnt = 0
isChange = False
for i in range(len(a)):
    if a[i] != b[i]:
        if not isChange:
            cnt += 1
            isChange = True
        else:
            isChange = False
print(cnt)