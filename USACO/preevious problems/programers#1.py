right = int(input('right:'))
left = int(input('left:'))

s = []
for i in range(right+1):
    s.append(i)
for j in range(left+1):
    s.append(-j)
print(sum(s))

