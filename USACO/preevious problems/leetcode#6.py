nums = list(map(int, input().split()))

dic = {}

for n in nums:
    if n not in dic:
        dic[n] = 1
    else:
        del dic[n]

print(list(dic.keys())[0])

